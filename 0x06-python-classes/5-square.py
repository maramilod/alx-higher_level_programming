#!/usr/bin/python3
"""python3"""


class Square:
    """method"""

    def __init__(self, size=0):
        """instantiation"""

        self.size = size

    @property
    def size(self):
        """getter"""

        return self.__size

    @size.setter
    def size(self, val):
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        if val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val

    def area(self):
        """2"""

        return self.__size ** 2

    def my_print(self):
        """squar"""

        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
