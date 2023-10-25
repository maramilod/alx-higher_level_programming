#!/usr/bin/python3
"""it is"""


class Square:
    """square"""

    def __init__(self, size=0, position=(0, 0)):
        """define"""

        self.size = size
        self.position = position

    def area(self):
        """2"""
        return self.__size * self.__size

    @property
    def size(self):
        """getter"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getter"""

        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int)
                or value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        """str"""

        if self.__size == 0:
            return ''
        string = self.__position[1] * '\n'
        for i in range(self.__size):
            string += self.__position[0] * ' ' + self.__size * '#'
            if i is not self.__size - 1:
                string += '\n'
        return string
