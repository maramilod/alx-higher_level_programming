#!/usr/bin/python3
def remove_char_at(str, n):
    lenght = len(str)
    for i in range(lenght):
        if i != n:
            s += str[i]
    return s
