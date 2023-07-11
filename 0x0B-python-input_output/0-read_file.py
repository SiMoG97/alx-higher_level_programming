#!/usr/bin/python3
"""read_file"""


def read_file(filename=""):
    """prints the content of a file

    Args:
        filename (str, optional): the file to be printed. Defaults to "".
    """
    with open(filename, "r", encoding="utf-8") as myFile:
        print(myFile.read())
