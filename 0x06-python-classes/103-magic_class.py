#!/usr/bin/python3
"""module"""
import math


class MagicClass:
    """magic"""
    def __init__(self, radius=0):
        """init"""
        self.__radius = 0
        if not isinstance(radius, float) and not isinstance(radius, int):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """circumference"""
        return 2 * math.pi * self.__radius
