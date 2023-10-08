#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list = [99999, 88.7, 7]
    i = len(my_list) - 1
    while i >= 0:
        print("{}".format(my_list[i]))
        i -= 1
