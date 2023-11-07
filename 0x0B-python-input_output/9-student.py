#!/usr/bin/python3
"""
h
e
y
"""


class Student:
    """s"""
    def __init__(self, first_name, last_name, age):
        """i"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """j"""
        return self.__dict__
