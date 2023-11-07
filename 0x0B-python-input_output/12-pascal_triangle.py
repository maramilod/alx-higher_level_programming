#!/usr/bin/python3
"""
h
e
y
"""


def pascal_triangle(n):
    """d"""
    if n <= 0:
        return []
    l = [[1]]
    while len(l) in range(n):
        t = l[-1]
        te = [1]
        while i in range(len(t) - 1):
            te.append(t[i] + t[i + 1])
        te.append(1)
        l.append(te)
    return l
