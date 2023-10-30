#!/usr/bin/python3
"""
h
e
y
"""


class Rectangle:
    """R"""

    number_of_instances = 0
    """n"""

    print_symbol = "#"
    """p s"""

    def __init__(self, width=0, height=0):
        """i"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """p g"""
        return self.__width

    @width.setter
    def width(self, value):
        """s w"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """p h"""
        return self.__height

    @height.setter
    def height(self, value):
        """s h"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """a"""
        return self.__width * self.__height

    def perimeter(self):
        """p"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """s"""
        string = ""
        if not self.width or not self.height:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") *
                self.height)[:-1]

    def __repr__(self):
        """return ala"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """d"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """b"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """square"""
        return cls(size, size)
