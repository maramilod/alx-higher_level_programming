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

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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
        if self.__width == 0:
            return hash_reg
        for i in range(self.__height):
            for j in range(self.__width):
                hash_reg += str(self.print_symbol)
            if i != self.__height - 1:
                hash_reg += "\n"
        return hash_reg

    def __repr__(self):
        """formal string representation of an instance"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """delete"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_2 if rect_2.area() > rect_1.area() else rect_1

    @classmethod
    def square(cls, size=0):
        """
        sq
        """
        return (cls(size, size))
