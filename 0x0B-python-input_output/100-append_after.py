#!/usr/bin/python3
"""append_agter"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing a specific string

    Args:
        filename (str, optional): the file name to insert to Defaults to "".
        search_string (str, optional): search string. Defaults to "".
        new_string (str, optional): the new line to insert. Defaults to "".
    """
    lines = []
    with open(filename, mode="r") as f:
        lines = f.readlines()
        linesCopy = lines[:]
        countLines = 0
        for line in linesCopy:
            countLines += 1
            if line.find(search_string) != -1:
                lines.insert(countLines, new_string)
                countLines += 1

    with open(filename, mode="w") as f:
        f.writelines(lines)
