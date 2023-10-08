#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list and len(my_list) != 0:
        new = []
        for i in my_list:
            new.append(True) if my_list[i] % 2 == 0 else new.append(False)
        return new
