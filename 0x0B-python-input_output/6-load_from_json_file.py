#!/usr/bin/python3
"""load_from_json_file"""
import json


def load_from_json_file(filename):
    """creates an Object FRoom a “JSON file”:

    Args:
        filename (any): file name to read frooom

    Returns:
        int: the object
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
