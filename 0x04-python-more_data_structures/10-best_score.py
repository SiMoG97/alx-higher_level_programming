#!/usr/bin/python3

def best_score(a_dictionary):
    if type(a_dictionary) is not dict:
        return None
    bestScore = None
    score = 0
    for key in a_dictionary:
        if score < a_dictionary[key]:
            score = a_dictionary[key]
            bestScore = key
    return bestScore
