#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniques = set(my_list)
    sum = 0
    for val in uniques:
        sum += val
    return sum
