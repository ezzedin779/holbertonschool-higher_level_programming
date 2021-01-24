#!/usr/bin/python3
""" checker ?"""


def is_same_class(obj, a_class):
    """ is the obj and a_class the same ?"""
    if isinstance(obj, a_class):
        return True
    return False
