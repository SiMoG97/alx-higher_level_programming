#!/usr/bin/python3
"""save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation:

    Args:
        my_obj (any): the object to write
        filename (any): file to be written at

    Returns:
        int: the number of characters written
    """
    with open(filename, mode="w") as f:
        return f.write(json.dumps(my_obj))
