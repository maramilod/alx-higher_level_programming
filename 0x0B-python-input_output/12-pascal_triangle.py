#!/usr/bin/python3
"""
h
e
y
"""


def pascal_triangle(n):
    """d"""

    triang = [[1]]
    if n <= 0:
        return []

    while len(triang) in range(n):
        t = triang[-1]
        te = [1]
        for i in range(len(t) - 1):
            te.append(t[i] + t[i + 1])
        te.append(1)
        triang.append(te)
    return triang
