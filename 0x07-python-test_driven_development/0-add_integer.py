#!/usr/bin/python3
"""
This module defines a function for adding two integers.

Module: add_integer

Functions:
    - add_integer(a, b=98): Adds two integers

"""


def add_integer(a, b=98):
    """Adds two integers

    Args:
        a (int): a number
        b (int, optional): a number. Defaults to 98.

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Returns:
        int: the sum of a and b
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
