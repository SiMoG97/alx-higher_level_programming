#!/usr/bin/python3
import sys


def addArgs():
    args = sys.argv
    result = 0
    for arg in args[1:]:
        result += int(arg)

    print("{}".format(result))


if __name__ == "__main__":
    addArgs()
