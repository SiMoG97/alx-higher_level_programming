#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    newMatrix = []
    for arr in matrix:
        newArr = []
        for num in arr:
            newArr.append(num * num)
        newMatrix.append(newArr)
    return newMatrix
