#!/usr/bin/python3
"""
h
e
y
"""
B = __import__("7-base_geometry").BaseGeometry


class Rectangle(B):
    """k"""
    def __init__(self, width, height):
        """i"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

