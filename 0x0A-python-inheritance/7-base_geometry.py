#!/usr/bin/python3
"""
h
e
y
"""


class BaseGeometry():
    """b"""
    def area(self):
        """s"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """i"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
