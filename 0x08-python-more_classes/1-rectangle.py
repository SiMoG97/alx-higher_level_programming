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
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrives the width attribute

        Returns:
            int: width value
        """
        return self.width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute.

        Args:
            value (int): a number

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.width = value

    @property
    def height(self):
        """Retrives the height attribute

        Returns:
            int: height value
        """
        return self.height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute.

        Args:
            value (int): a number

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.height = value
