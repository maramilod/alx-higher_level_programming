#!/usr/bin/python3
"""square"""


class Square:
    """define"""

    def __init__(self, size=0):
        """con..."""

        if not size.isint():
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
