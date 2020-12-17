#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        name = ""
        best = 0
        for i in a_dictionary:
            if a_dictionary[i] > best:
                best = a_dictionary[i]
                name = i
        return name
    else:
        return None
