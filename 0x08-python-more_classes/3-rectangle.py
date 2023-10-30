#!/usr/bin/python3
"""
h
e
y
"""


class Rectangle:
    """
    empty
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ height * width """
        return self.height * self.width

    def perimeter(self):
        """ 0 or the sum """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height * 2) + (self.width * 2)

    def __str__(self):
        """informal string representation of an instance"""
        hash_reg = ""
        for i in range(self.height):
            for j in range(self.width):
                hash_reg += "#"
            if i != self.height - 1:
                hash_reg += "\n"
        return hash_reg
