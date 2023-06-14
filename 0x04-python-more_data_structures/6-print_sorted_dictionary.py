#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sortedKeys = list(a_dictionary.keys())
    sortedKeys.sort()
    for key in sortedKeys:
        print("{}: {}".format(key, a_dictionary.get(key)))
