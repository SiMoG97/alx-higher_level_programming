#!/usr/bin/python3
"class Rectangle that inherits BaseGeometry"
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of a Rectangle

        Returns:
            int: the area
        """
        return self.__width * self.__height

    def __str__(self):
        """ [Rectangle] <width>/<height>

        Returns:
            str: "[Rectangle] <width>/<height>"
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
