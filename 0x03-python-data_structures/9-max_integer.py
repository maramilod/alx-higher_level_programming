#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) > 0 and my_list:
        maxx =  my_list[0]
        for i in range(len(my_list)):
            if maxx < my_list[i]:
                maxx = my_list[i]
        return maxx
    return None
