#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """a function that prints a text with 2 new lines after
        each of these characters: ., ? and :

    Args:
        text (str): the string to be printed

    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] == " " and text[i - 1] in [".", "?", ":"]:
            continue

        print("{}".format(text[i]), end="")
        if text[i] in [".", "?", ":"]:
            print("\n")
