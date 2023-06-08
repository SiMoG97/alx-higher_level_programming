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

    result = 0
    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = sub(a, b)
    elif op == "*":
        result = mul(a, b)
    else:
        result = div(a, b)

    print("{} {} {} = {}".format(a, op, b, result))


if __name__ == "__main__":
    calculator()
