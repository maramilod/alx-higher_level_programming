#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list and my_list != []:
        maxx =  my_list[0]
        for i in range(1, len(my_list)):
            if maxx < my_list[i]:
                maxx = my_list[i]
        return maxx
    return None
