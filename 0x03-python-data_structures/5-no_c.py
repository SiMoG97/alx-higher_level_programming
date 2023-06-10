#!/usr/bin/python3

def no_c(my_string):
    newStr = ""
    for c in my_string:
        if c == 'c' or c == 'C':
            continue
        newStr += c
    return newStr
