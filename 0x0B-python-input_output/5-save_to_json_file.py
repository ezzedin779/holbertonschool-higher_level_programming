#!/usr/bin/python3
""" save to json file"""
import json


def save_to_json_file(my_obj, filename):
    """ Python object"""
    with open(filename, mode='w') as f:
        json.dump(my_obj, f)
