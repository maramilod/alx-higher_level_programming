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
            li = f.readline()
            if line == "":
                break
            line.append(li)
            if search_string in li:
                line.append(new_string)
    with open(filename, "w", encoding="utf-8") as m:
        m.writelines(line)
