#!/usr/bin/python3
"""
This module defines a function for dividing a matrix.

Module: matrix_divided

Functions:
    - matrix_divided(matrix, div): divided a matrix by div
"""


def matrix_divided(matrix, div):
    """A function that returns a matrix of the divided int float values
        of the input matrix by div

    Args:
        matrix (list[list[int]]): a matrix of int or flaot number
            with rows of the same length
        div (int, float): the divider

    Raises:
        TypeError: div must be a number
        ZeroDivisionError: division by zero
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size

    Returns:
        list[list[int]]: a matrix of divided elements by div of input matrix
    """

    newMatrix = []
    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    err_row = "Each row of the matrix must have the same size"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or not isinstance(matrix[0], list):
        raise TypeError(err_matrix)

    listLen = len(matrix[0])

    for i in range(len(matrix)):
        newList = []
        if not isinstance(matrix[i], list):
            raise TypeError(err_matrix)

        if len(matrix[i]) != listLen:
            raise TypeError(err_row)

        for num in matrix[i]:
            if not isinstance(num, (int, float)):
                raise TypeError(err_matrix)

            newList.append(round(num / div, 2))
        newMatrix.append(newList)

    return newMatrix
