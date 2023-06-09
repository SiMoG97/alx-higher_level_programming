#!/usr/bin/python3

"""
This module defines a class and functions related to squares.
"""


class Rectangle:
    """A class that represents a Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ a method that returns the area of The rectangle

        Returns:
            int: the area of the Rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Method that returns the rectangle perimeter

        Returns:
            int: rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """a string representation of the object,
        representing a rectangle made of '#' symbols.

        Returns:
            str: A string representing the rectangle with '#' symbols.
        """
        mystr = ""
        for h in range(self.__height):
            for w in range(self.__width):
                mystr += str(self.print_symbol)
                if w == self.__width - 1 and h != self.__height - 1:
                    mystr += "\n"
        return mystr

    def __repr__(self):
        """Returns a string representation of the object
        that can be used to recreate the Rectangle object.

        Returns:
            str: A string representing the Rectangle object in the format
            "Rectangle(width, height)".
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Print the message 'Bye rectangle...'
        when an instance of Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method that returns the biggest rectangle based on the area

        Args:
            rect_1 (Rectangle): Rectangle 1
            rect_2 (Rectangle): Rectangle 2

        Raises:
            TypeError: rect_1 must be an instance of Rectangle
            TypeError: rect_2 must be an instance of Rectangle

        Returns:
            Rectangle: The biggest rectangle of the two
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Class method that returns a new Rectangle instance
        with width == height == size

        Args:
            size (int, optional): size of width and height. Defaults to 0.

        Returns:
            Rectangle: a new Rectangle instance
        """
        return cls(size, size)
