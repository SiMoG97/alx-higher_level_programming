#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        ld = number % -10
        ld *= -1
    else:
        ld = number % 10
    print("{}".format(ld), end="")
    return ld
