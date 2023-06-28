#!/usr/bin/python3

"""
This module defines a class and functions related to squares.
"""


class Square:
    """A class representing a square."""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object with the specified size.

        Args:
            size: The size (length of a side) of the square.
            position (tuple): The position of the square. Defaults to (0, 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

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
            return

        for _ in range(self.position[1]):
            print("")

        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                print(" ", end="")

            for j in range(self.__size):
                print("#", end="")
                if j == self.__size - 1:
                    print("")

    @property
    def position(self):
        """
        Getter method for the position attribute.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.

        Args:
            value (tuple): The new position to set, as a tuple of 2 ints
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("Position must be a tuple of 2 positive integers")

        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError("Position must be a tuple of 2 positive integers")
        self.__position = value
