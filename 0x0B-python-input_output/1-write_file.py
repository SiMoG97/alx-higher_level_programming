#!/usr/bin/python3
"""write_file"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8)
    and returns the number of characters written:

    Args:
        filename (str, optional): file name to write to. Defaults to "".
        text (str, optional): the text to be written. Defaults to "".

    Returns:
        int: the number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
