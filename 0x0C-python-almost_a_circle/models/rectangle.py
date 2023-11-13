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
        """i"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """area"""
        return self.width * self.height

    def display(self):
        """'update' draw rectangle"""
        self.width += self.x
        for y in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.width):
                if j >= self.x:
                    print("#", end="")
                else:
                    print(" ", end="")
            print()

    def __str__(self):
        """overriding"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """updated data"""
        if len(args) >= 5:
            self.id, self.width, self.height, self.x, self.y = args
        elif len(args) == 4:
            self.id, self.width, self.height, self.x = args
        elif len(args) == 3:
            self.id, self.width, self.height = args
        elif len(args) == 2:
            self.id, self.width = args
        elif len(args) == 1:
            self.id = args[0]
        else:
            for k, v in kwargs.items():
                if k == "width":
                    self.width = v
                if k == "height":
                    self.height = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v
                if k == "id":
                    self.id = v

    def to_dictionary(self):
        """d"""
        di = {
                "x": self.x,
                "y": self.y,
                "id": self.id,
                "height": self.height,
                "width": self.width
                }
        return di
