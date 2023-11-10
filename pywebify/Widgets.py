from pywebify.Web import NewPage

class _Element():
    """
    Base class for GUI elements.

    Attributes:
        master (NewPage): The parent page.
        width (int): The width of the element.
        height (int): The height of the element.
        widget_type (str): The type of widget (set to None by default).
        attrs (dict): A dictionary of attributes for the element, including 'x', 'y', 'h', and 'w'.
    """
    def __init__(self, master: NewPage, width=150, height=150):
        self.master = master
        self.widget_type = None
        self.attrs = {"x": 0, "y": 0, "h": height, "w": width}

    def pack(self, *args, **kwargs):
        """
        Pack the element within its parent.

        Args:
            *args: Variable positional arguments.
            **kwargs: Variable keyword arguments.
        """
        print(self.master.attributes)

    def place(self, *args, **kwargs):
        """
        Place the element at specific coordinates within its parent.

        Args:
            *args: Variable positional arguments.
            **kwargs: Variable keyword arguments.
        """
        pass

    def grid(self, *args, **kwargs):
        """
        Grid layout for the element within its parent.

        Args:
            *args: Variable positional arguments.
            **kwargs: Variable keyword arguments.
        """
        pass

    def config(self, attr, change):
        """
        Configure an attribute of the element.

        Args:
            attr (str): The attribute to be changed.
            change: The new value for the attribute.

        Returns:
            bool: True if the attribute is successfully changed, False otherwise.
        """
        try:
            self.attrs[attr] = change
            return True
        except:
            return False

class Label(_Element):
    """
    Class for creating label elements.

    Attributes:
        master (NewPage): The parent page.
        text (str): The text to be displayed on the label.
        px (int): The font size in pixels.
        font (str): The font type.
        width (int): The width of the label.
        height (int): The height of the label.
    """
    def __init__(self, master: NewPage, text, px=24, font="Ariel", width=150, height=150):
        super().__init__(master, width, height)
        self.attrs["px"] = int(px)
        self.attrs["font"] = str(font)
        self.attrs["text"] = str(text)
        self.widget_type = type(self).__name__
        self.master.attributes["template"]["html"].append(self)

    def __repr__(self):
        return f"Label('{self.attrs['text']}', '{self.attrs['font']}', {self.attrs['px']}, {self.attrs['x']}, {self.attrs['y']}, {self.attrs['w']}, {self.attrs['h']})"

class Image(_Element):
    """
    Class for creating image elements.

    Attributes:
        master (NewPage): The parent page.
        path (str): The path to the image file.
        width (int): The width of the image.
        height (int): The height of the image.
    """
    def __init__(self, master: NewPage, path, width=150, height=150):
        super().__init__(master, width, height)
        self.attrs["path"] = path
        self.attrs["alt"] = 'Untagged Image'
        self.widget_type = type(self).__name__
        self.master.attributes["template"]["html"].append(self)

    def __repr__(self):
        return f"Image({self.attrs['path']}, {self.attrs['alt']}, {self.attrs['x']}, {self.attrs['y']}, {self.attrs['w']}, {self.attrs['h']})"

class Frame(_Element):
    """
    Class for creating frame elements.

    Attributes:
        master (NewPage): The parent page.
        color (str): The background color of the frame.
        border_radius (int): The border radius of the frame.
        width (int): The width of the frame.
        height (int): The height of the frame.
    """
    def __init__(self, master: NewPage, color, border_radius=0, width=150, height=150):
        super().__init__(master, width, height)
        self.attrs["border-radius"] = border_radius
        self.attrs["color"] = color
        self.widget_type = type(self).__name__
        self.master.attributes["template"]["html"].append(self)

    def __repr__(self):
        return f"Frame({self.attrs['rounded']}, {self.attrs['color']}, {self.attrs['x']}, {self.attrs['y']}, {self.attrs['w']}, {self.attrs['h']})"
