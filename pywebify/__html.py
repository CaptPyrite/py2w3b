import ast

class html_translate():
    """
    Class for translating elements into HTML and CSS code.

    Attributes:
        funcs (dict): A dictionary to store translation functions for different element types.
    """
    def __init__(self):
        self.funcs = {}
        
    def new_prefix(self, func):
        """
        Register a new translation function.

        Args:
            func (function): The translation function to be registered.
        """
        def wrap(*args):
            self.funcs[func.__name__] = func
        wrap()
        
    def compile(self, elements):
        """
        Compile a list of elements into HTML and CSS code.

        Args:
            elements (list): A list of elements to be translated.
        """
        for element in elements:
            prefix = str(element).split("(")[0]
            
            if prefix in self.funcs:
                repr_str = repr(element)
                formatted_str = repr_str.replace(f"{prefix}(", "[").replace(")", "]")
                real_list = ast.literal_eval(formatted_str)
                out_ = self.funcs[prefix](real_list)
                
                print(out_)
                
def translate(pages):
    """
    Translate pages into HTML and CSS code.

    Args:
        pages (dict): A dictionary of pages and their templates.
    """
    translator = html_translate()
    
    @translator.new_prefix
    def Label(specs: list):
        """
        Translate Label element specifications into HTML.

        Args:
            specs (list): A list of specifications for the Label element.

        Returns:
            tuple: A tuple containing the type ("HTML") and the translated HTML code.
        """
        text_ = specs[0]
        font_ = specs[1]
        font_s = specs[2]  # font size, px
        return ("HTML", f'<p style="font-family:{font_};font-size:{font_s}px">{text_}</p>')

    @translator.new_prefix
    def Image(specs: list):
        """
        Translate Image element specifications into HTML.

        Args:
            specs (list): A list of specifications for the Image element.

        Returns:
            tuple: A tuple containing the type ("HTML") and the translated HTML code.
        """
        path_ = specs[0]
        alt_ = specs[1]
        w, h = specs[4], specs[5]
        return ("HTML", f'<img src="{path_}" alt="{alt_}" width="{w}" height="{h}">')

    @translator.new_prefix
    def Frame(specs: list):
        """
        Translate Frame element specifications into CSS.

        Args:
            specs (list): A list of specifications for the Frame element.

        Returns:
            tuple: A tuple containing the type ("CSS") and the translated CSS code.
        """
        border_radius_ = specs[0]
        bg_ = specs[1]
        w, h = specs[4], specs[5]
        return ("CSS", """
                #rcorners1 {
                    border-radius: {0};
                    background: {1}; 
                    width: {3};
                    height: {4};  
                }
                """.strip().format(border_radius_, bg_, w, h))

    for route in pages:
        page = pages[route]["template"]
        translator.compile(page["html"])
