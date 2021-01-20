#!/usr/bin/python3
""" read a file """


def read_file(filename=""):
    """ what do u have in mind ?"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
