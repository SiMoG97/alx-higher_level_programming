#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastD = number % 10

if (number < 0):
    lastD = number % -10

if (lastD == 0):
    print(f"Last digit of {number} is {lastD} and is {lastD}")
elif (lastD > 5):
    print(f"Last digit of {number} is {lastD} and is greater than 5")
elif (lastD < 6):
    print(f"Last digit of {number} is {lastD} and is less than 6 and not 0")
