#!/usr/bin/python3
"""python3"""


class Square:
    """method"""

    def __init__(self, size=0, position=(0, 0)):
        """instantiation"""

        self.size = size
        self.position = position

    @property
    def position(self):
        """getter"""

        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

        if self.__size == 0:
            print()
            return

        [print() for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print()
