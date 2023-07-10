#!/usr/bin/python3

"""This module has a function that returns the list
of available attr and methos of an object"""


def lookup(obj):
    """a function that returns the list of available
    attributes and methods of an object

    Args:
        obj (any): any object

    Returns:
        list: list object
    """
    return dir(obj)
