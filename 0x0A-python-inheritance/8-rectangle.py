#!/usr/bin/python3
"""Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherits all methods and attr of BaseGeometry"""

    def __init__(self, width, height):
        """Instantiate a new Rectangle

        Args:
            width (int): the width of the rect
            height (int): the height of the rect
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
