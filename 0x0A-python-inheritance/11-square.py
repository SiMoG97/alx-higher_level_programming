#!/usr/bin/python3
"class Square that inherits Rectangle class"
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherits all methods and attr of Rectangle"""

    def __init__(self, size):
        """initilize Square objects

        Args:
            size (int): the size of the Square
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns the area of the square

        Returns:
            int: the area of the sqaure
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns:
            str: [Square] width/height
        """
        return f"[Square] {self.__size}/{self.__size}"
