#!/usr/bin/python3

import sys


def printArgs():
    argsLen = len(sys.argv) - 1
    printS = "s" if argsLen != 1 else ""
    printDots = "." if argsLen == 0 else ":"
    print("{} argument{}{}".format(argsLen, printS, printDots))
    i = 0
    for arg in sys.argv:
        if i == 0:
            i += 1
            continue
        print("{}: {}".format(i, arg))
        i += 1

if __name__ == "__main__":
    printArgs()
