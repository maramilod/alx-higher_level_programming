#!/usr/bin/python3
def magic_string():
    magic_string.co = getattr(magic_string, "co", 0) + 1
    return ", ".join(["BestSchool" for i in range(magic_string.co)])
