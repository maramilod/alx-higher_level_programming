#!/usr/bin/python3
"""^-^"""


class Square:
    """O-O"""

    def __init__(self, size=0):
        """ini"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area"""

        return self.__size ** 2

    def __ge__(self, other):
        """grater or equal"""

        if (isinstance(other, Square)):
            return self.area() >= other.area()

    def __le__(self, other):
        """less or equal"""

        if (isinstance(other, Square)):
            return self.area() <= other.area()

    def __ne__(self, other):
        """not"""

        if (isinstance(other, Square)):
            return self.area() != other.area()

    def __eq__(self, other):
        """equal"""

        if (isinstance(other, Square)):
            return self.area() == other.area()

    def __lt__(self, other):
        """less than"""

        if (isinstance(other, Square)):
            return self.area() < other.area()

    def __gt__(self, other):
        """greater than"""

        if (isinstance(other, Square)):
            return self.area() > other.area()

    @property
    def size(self):
        """getter"""

        return self.__size

    @size.setter
    def size(self, val):
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = val
