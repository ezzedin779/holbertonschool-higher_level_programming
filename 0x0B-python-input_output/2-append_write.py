#!/usr/bin/python3
""" appending in a file"""


def append_write(filename="", text=""):
    """ append """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
