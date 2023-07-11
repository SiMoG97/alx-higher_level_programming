#!/usr/bin/python3

"""Rectangle class"""


class Rectangle(BaseGeometry):
    """Rectangle class inherits all methods and attr of BaseGeometry"""

    def __init__(self, width, height):
        """Instantiate a new Rectangle

        Args:
            width (int): the width of the rect
            height (int): the height of the rect 
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.height = height
