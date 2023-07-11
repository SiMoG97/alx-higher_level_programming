#!/usr/bin/python3
"""class_to_json"""


def class_to_json(obj):
    """a function that returns the dictionary description with simple
    data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    Args:
        obj (object): an instance of a class

    Returns:
        dict: dictionary representation of obj.
    """
    return obj.__dict__
