#!/usr/bin/python3
"""
h
e
y
"""
import json


def save_to_json_file(my_obj, filename):
    """s"""
    with open(filename, "w", encoding="utf-8") as m:
        json.dump(my_obj, m)
