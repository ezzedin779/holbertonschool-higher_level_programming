#!/usr/bin/python3
""" write in a file """


def write_file(filename="", text=""):
    """ write that """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
