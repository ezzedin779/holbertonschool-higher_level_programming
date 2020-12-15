#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        c = (0, None)
        return c
    else:
        c = (len(sentence), sentence[0])
        return c
