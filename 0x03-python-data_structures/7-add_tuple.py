#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    firstA = tuple_a[0] if len(tuple_a) > 0 else 0
    secA = tuple_a[1] if len(tuple_a) > 1 else 0

    firstB = tuple_b[0] if len(tuple_b) > 0 else 0
    secB = tuple_b[1] if len(tuple_b) > 1 else 0

    return (firstA + firstB, secA + secB)
