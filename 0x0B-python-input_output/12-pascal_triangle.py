#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascals triangle of n

    Args:
        n (_type_): the number of lists in list

    Returns:
        list: list of lists of integers
    """
    if n <= 0:
        return []

    myList = []
    for i in range(n):
        innerList = []
        for j in range(i + 1):
            try:
                if j == i or j == 0:
                    innerList.append(1)
                    continue
                num = myList[i - 1][j] + myList[i - 1][j - 1]
                innerList.append(num)
            except IndexError:
                innerList.append(1)

        myList.append(innerList)
    return myList
