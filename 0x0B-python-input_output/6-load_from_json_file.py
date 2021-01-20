#!/usr/bin/python3
""" loading from a file ?"""
import json


def load_from_json_file(filename):
    """ Python object"""
    with open(filename) as f:
        return json.load(f)
