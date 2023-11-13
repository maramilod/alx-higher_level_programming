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
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y,
                self.width)
