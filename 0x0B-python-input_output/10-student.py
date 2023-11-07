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

    def to_json(self, attrs=None):
        """j"""
        try:
            for i in attrs:
                if type(i) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        dr = dict()
        for k, v in self.__dict__items:
            if k in attrs:
                dr[k] = v
        return dr
