#!/usr/bin/python3
"""
h
e
y
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """sup class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """s"""
        return self.width

    @size.setter
    def size(self, value):
        """s"""
        self.width = value
        self.height = value

    def __str__(self):
        """'Returns string info about this square"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y,
                self.width)

    def update(self, *args, **kwargs):
        """Updates instance attributes via no-keyword & keyword args"""
        if args is not None and len(args) != 0:
            if len(args) >= 4:
                self.id, self.width, self.x, self.y = args
            elif len(args) == 3:
                self.id, self.width, self.x = args
            elif len(args) == 2:
                self.id, self.width = args
            elif len(args) == 1:
                self.id = args[0]
        else:
            for k, v in kwargs.items():
                if k == "size":
                    self.width = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v
                if k == "id":
                    self.id = v

    def to_dictionary(self):
        """Returns dictionary representation of this class"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
