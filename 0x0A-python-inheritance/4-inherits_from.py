#!/usr/bin/python3

"""a function"""


def inherits_from(obj, a_class):
    """a function that returns True if the object is
    an instance of, or if the object is an instance
    of a class that inherited from,
    the specified class ; otherwise False

    Args:
        obj (any): some obj
        a_class (any): some class

    Returns:
        boolean: True if obj is instance of a_class, otherwise false
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

