#!/usr/bin/python3
"""
h
e
y
"""


def append_after(filename="", search_string="", new_string=""):
    """a"""
    with open(filename, 'r', encoding="utf-8") as m:
        line = []
        while True:
            l = f.readline()
            if line = "":
                break
            line.append(l)
            if search_string in l:
                line.append(new_string)
    with open(filename, "w", encoding="utf-8") as m:
        m.writelines(line)
