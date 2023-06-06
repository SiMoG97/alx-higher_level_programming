#!/usr/bin/python3

def uppercase(str):
    char = 0
    for c in str:
        if (ord(c) >= ord('a') and ord(c) <= ord('z')):
            char = ord(c) - 32
        else:
            char = ord(c)

        print("{}".format(chr(char)), end="")
    print("")
