#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) != 0:
        maxx =  my_list[0]
        for i in my_list:
            maxx = i if i > maxx else maxx
        return maxx
    return None
