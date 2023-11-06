#!/usr/bin/python3
"""
h
e
y
"""
R = __import__("9-rectangle").Rectangle


class Square(R):
    """s"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """a"""
        return self.__size ** 2

    def __str__(self):
        """s"""
        return "[Square] {}/{}".format(
                str(self.__size), str(self.__size))
