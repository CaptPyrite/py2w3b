from typing import Any
import flask
import textwrap
from . import __interpreter as HTMLLIB

class NewSite:
    """
    Class representing a website using Flask.

    Attributes:
        pages (dict): A dictionary to store pages and their templates.
        app (Flask): The Flask application instance.
    """
    def __init__(self, host="localhost:8080", name=__name__):
        """
        Initialize a NewSite object.

        Args:
            host (str): The host and port to run the website (default is "localhost:8080").
            name (str): The name of the application (default is the current module's name).
        """
        self.pages = {}
        self.app = flask.Flask(name)
        
    def mainloop(self, nodir=True):
        """
        Start the website and serve the pages.

        Args:
            nodir (bool): Not used in the provided code, could be documented further.
        """
        # Compiles the HTML
        HTMLLIB.translate(self.pages)
        
        
        # Renders everything
        for page_num, page_url in enumerate(self.pages):
            endpoint_function_name = f"render_page_{page_num}"
            route_definition = f"""
                @self.app.route('{page_url}')
                def {endpoint_function_name}():
                    return '''
                    <head>
                        <title>{self.pages[page_url]['title']}</title>
                    </head>
                    
                    <body>
                        {''.join(map(str, self.pages[page_url]['template']['html']))}
                    </body>
                    
                    <style>
                        {''.join(map(str,self.pages[page_url]['template']['style']))}                    
                    </style>
                    
                    <script>
                        {''.join(map(str,self.pages[page_url]['template']['js']))}
                    </script>
                    '''
                """
            formatted_code = textwrap.dedent(route_definition).strip()
            
            exec(formatted_code)
            
        self.app.run()
        
                
    def _testloop(self):
        """
        Test loop for translating page templates using HTMLLIB.translate.

        Not used in the provided code, could be documented further.
        """
        HTMLLIB.translate(self.pages)
        print(self.pages)
        
        
class NewPage:
    """
    Class representing a page on the website.

    Attributes:
        attributes (dict): A dictionary containing page attributes and templates.
        NewSite (NewSite): The parent NewSite object.
        route (str): The route or URL path of the page.
    """
    def __init__(self, master: NewSite, route, title:str="Untitled Page"):
        """
        Initialize a NewPage object.

        Args:
            master (NewSite): The parent NewSite object.
            route (str): The route or URL path of the page.
        """
        self.attributes = {"title": title,
                           "template": {
                               "html": [],
                               "style": [],
                               "js": [],
                               "static": []
                               }
                           }
        if route == "__main__":
           route = "/"

        master.pages[route] = self.attributes
        
        
