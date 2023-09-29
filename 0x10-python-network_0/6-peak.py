#!/usr/bin/python3
"""_summary_
"""


def find_peak(list_of_integers):
    """_summary_

    Args:
        list_of_integers (_type_): _description_
    """
    if len(list_of_integers) == 0:
        return None
    peak = list_of_integers[0]

    for num in list_of_integers:
        if num > peak:
            peak = num
    return peak
