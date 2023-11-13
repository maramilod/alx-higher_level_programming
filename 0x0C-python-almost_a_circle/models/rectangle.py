#!/usr/bin/python3
"""
h
e
y
"""
from models.base import Base

class Rectangle(Base):
    """class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width


    @property
    def width(self):
        return self.__width


    @width.setter
    def width(self, width):
        self.__width = width


    @property
    def height(self):
        return self.__height


    @height.setter
    def height(self, height):
        self.__height = height


    @property
    def x(self):
        return self.__x


    @x.setter
    def x(self, x):
        self.__x = x


    @property
    def y(self, y):
        return self.__y


    @y.setter
    def y(self):
        self.__y = y

