#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1
    i = number
    while i > 9:
        i %= 10
    print(i, end="")
    return i
