#!/usr/bin/python3
"""
this class will be
the base of all other
classes in this project
to manage id attribute
and avoid duplicating
"""
import json

class Base:
    """ the base of python package """

    __nb_objects = 0

    def __init__(self, id=None):
        """i"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """t"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """s"""
        new_li = []
        if list_objs is not None:
            for i in list_objs:
                new_li.append(i.to_dictionary())
        with open(cls.__name__ + ".json",
                "w+", encoding="utf-8") as file:
            file.write(Base.to_json_string(new_li))
