#!/usr/bin/python3

"""
This module defines a class and functions related to squares.
"""


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """
        Initializes a Square object with the specified size.

        Args:
            size: The size (length of a side) of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """Print a square pattern of '#' characters."""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
                if j == self.__size - 1:
                    print("")
