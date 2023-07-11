#!/usr/bin/python3
"""from_json_string"""
import json


def from_json_string(my_str):
    """Converts JSON to object.

    Args:
        my_str (str): String object to be serialized.

    Return:
        any: the object
    """
    return json.loads(my_str)
