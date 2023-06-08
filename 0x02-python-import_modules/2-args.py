#!/usr/bin/python3

import sys


def printArgs():
    argsLen = len(sys.argv) - 1
    printS = "s" if argsLen != 1 else ""
    printDots = "." if argsLen == 0 else ":"
    print("{} argument{}{}".format(argsLen, printS, printDots))

    for i, arg in enumerate(sys.argv, 1):
        print("{}: {}".format(i - 1, arg))


if __name__ == "__main__":
    printArgs()
