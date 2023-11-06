#!/usr/bin/python3
"""
h
e
y
"""


def add_attribute(o, a, v):
    """a"""
    if not hasattr(o, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(o, a, v)
