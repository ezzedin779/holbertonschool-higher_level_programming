#!/usr/bin/python3
""" Another type of checker"""


def inherits_from(obj, a_class):
    """ using subclass """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
