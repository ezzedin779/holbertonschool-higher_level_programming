#!/usr/bin/python3
""" SAVE ALL ARGS IN FILE """
from sys import argv
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


f_n = "add_item.json"
try:
    my_list = load(f_n)
except:
    my_list = []
for arg in argv[1:]:
    my_list.append(arg)
save(my_list, f_n)
