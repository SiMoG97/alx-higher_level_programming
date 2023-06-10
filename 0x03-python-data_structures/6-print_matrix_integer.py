#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for xList in matrix:
        for i, num in enumerate(xList):
            terminator = " "
            if i == len(xList) - 1:
                terminator = ""
            print("{:d}".format(num), end=terminator)
        print("")
