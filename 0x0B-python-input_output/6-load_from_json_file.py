#!/usr/bin/python3
"""
h
e
y
"""
import json


def load_from_json_file(filename):
    """l"""
    with open(filename, "r", encoding="utf-8") as m:
        return json.load(m)
