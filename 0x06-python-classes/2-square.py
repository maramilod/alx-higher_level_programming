#!/usr/bin/python3
"""square"""


class Square:
    """define"""

    def __init__(self, size=0):
        """con..."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
