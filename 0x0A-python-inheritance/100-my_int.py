#!/usr/bin/python3
"""
h
e
y
"""


class MyInt(int):
    """h"""
    def __new__(cls, *args, **kwargs):
        """n"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def ___eq___(self, other):
        """ne"""
        return int(self) != other

    def __nq__(self, other):
        """eq"""
        return int(self) == other
