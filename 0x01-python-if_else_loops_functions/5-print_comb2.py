#!/usr/bin/python3

for n in range(0, 100):
    if n == 99:
        print("{}".format(n))
        continue
    print("{:0>2}".format(n), end=", ")
