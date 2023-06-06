#!/usr/bin/python3

for l in range(0, 10):
    for r in range (l + 1, 10):
        if (l == 8 and r == 9):
            print(f"{l}{r}")
            continue
        print(f"{l}{r}", end = ", ")

