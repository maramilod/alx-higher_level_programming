#!/usr/bin/python3
"""hey ^-^"""


class Square:
    """-_-"""

    def __init__(self, size=0):
        """*-*"""

        self.size = size

    @property
    def size(self):
        """pro"""

        return self.__size

    @size.setter
    def size(self, val):
        if not isinstance(val, int):
            raise TypeError("")
        if val < 0:
            raise ValueError("")
        self.__size = val

    def erea(self):
        """hey again"""

        return self.__size ** 2
