#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def calculator():
    args = sys.argv
    argsLen = len(args) - 1

    if argsLen != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = args[2]
    if op != "+" and op != "/" and op != "*" and op != "-":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(args[1])
    b = int(args[3])

    if op == "+":
        print("{} {} {} = {}".format(a, op, b, add(a, b)))
    elif op == "-":
        print("{} {} {} = {}".format(a, op, b, sub(a, b)))
    elif op == "*":
        print("{} {} {} = {}".format(a, op, b, mul(a, b)))
    else:
        print("{} {} {} = {}".format(a, op, b, div(a, b)))


if __name__ == "__main__":
    calculator()
