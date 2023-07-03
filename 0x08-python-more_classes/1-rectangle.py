#!/usr/bin/python3

"""
This module defines a class and functions related to squares.
"""


class Rectangle:
    """A class that represents a Rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiation

        Args:
            width (int, optional): width value. Defaults to 0.
            height (int, optional): height value. Defaults to 0.
        """
        self._posIntCheck(width, "width")
        self._posIntCheck(height, "height")

        self.__width = width
        self.__height = height

    def _posIntCheck(self, value, attrName):
        """_summary_

        Args:
            value (int): a number to check
            attrName (str): the attribute's name

        Raises:
            TypeError: {attributeName} must be integer
            ValueError: {attributeName} must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attrName))

        if value < 0:
            raise ValueError("{} must be >= 0".format(attrName))

    @property
    def width(self):
        """Retrives the width attribute

        Returns:
            int: width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute.

        Args:
            value (int): a number
        """
        self._posIntCheck(value, "width")

        self.__width = value

    @property
    def height(self):
        """Retrives the height attribute

        Returns:
            int: height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute.

        Args:
            value (int): a number
        """
        self._posIntCheck(value, "height")

        self.__height = value
