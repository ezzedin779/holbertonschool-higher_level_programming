#!/usr/bin/python3
def weight_average(my_list=[]):
    if not(my_list):
        return 0
    s = 0
    p = 0
    for j in my_list:
        p += j[0] * j[1]
        s += j[1]
    return p/s
