#!/usr/bin/python3
"""med"""


class Square:
    """con"""

    def __init__(self, size=0):
        """def"""

        if not isinstance(size, int):
            raise TypeError("")
        if size < 0:
            raise ValueError("")
        self.__size = size

    def area(self):
        """area of the square"""

        return self.__size * self.__size
