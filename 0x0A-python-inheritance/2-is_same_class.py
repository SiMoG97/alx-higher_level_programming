#!/usr/bin/python3

"""A function"""


def is_same_class(obj, a_class):
    """a function that returns True if the object is exactly
    an instance of the specified class ; otherwise False.

    Args:
        obj (any): _description_
        a_class (any): _description_

    Returns:
        boolean: true if an instance of a_class otherwise false
    """
    return type(obj) is a_class
