#!/usr/bin/python3
"""
this class will be
the base of all other
classes in this project
to manage id attribute
and avoid duplicating
"""


class Base:
    """ the base of python package """

    __nb_objects = 0
    def __init__(self, id=None):
        """i"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
