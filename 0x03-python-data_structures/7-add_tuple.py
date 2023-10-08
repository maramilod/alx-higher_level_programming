#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a == ():
        if tuple_b == ():
            return None
        return tuple_b[0], tuple_b[1]
    if tuple_b == ():
        if tuple_a == ():
            return None
        return tuple_a[0], tuple_a[1]
    b = 0
    a = tuple_a[0] + tuple_b[0]
    if len(tuple_a) > 1:
        b += tuple_a[1]
    if len(tuple_b) > 1:
        b += tuple_b[1]
    return a, b
