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
        """constructior i n i t"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """width getter"""
        return self.width

    @size.setter
    def size(self, value):
        """width setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """formated string"""
        id = self.id
        size = self.width
        x = self.x
        y = self.y
        return "[Square] ({}) {}/{} - {}".format(id, x, y, size)

    def update(self, *args, **kwargs):
        """updates"""
        if args is not None and len(args) != 0:
            a = len(args)
            if a >= 1:
                self.id = args[0]
            if a >= 2:
                self.size = args[1]
            if a >= 3:
                self.x = args[2]
            if a >= 4:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """dict"""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
