#!/usr/bin/python3
"""To JSON String"""
import json


def to_json_string(my_obj):
    """Converts a string object to JSON.

    Args:
        my_obj (str): String object to be serialized.

    Return:
        str: the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
