#!/usr/bin/python3
"""
h
e
y
"""
from models.rectangle  import Rectangle

class Square(Rectangle):
    """sup class"""

    def __init__(self, size, x=0, y=0, id=None):
        """i"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        """s"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y,
                self.width)

    def update(self, *args, **kwargs):
        """update"""
        if len(args) >= 4:
            self.id, self.width, self.x, self.y = args
        elif len(args) == 3:
            self.id, self.width, self.x = args
        elif len(args) == 2:
            self.id, self.width = args
        elif len(args) == 1:
            self.id = args[0]
        else:
            for k , v in kwargs.items():
                if k == "size":
                    self.width = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v
                if k == "id":
                    self.id = v
