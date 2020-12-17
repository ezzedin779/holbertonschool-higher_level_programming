#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not(a_dictionary):
        return a_dictionary
    dic_list = list(a_dictionary.items())
    for i, j in dic_list:
        if j == value:
            del a_dictionary[i]
    return a_dictionary
