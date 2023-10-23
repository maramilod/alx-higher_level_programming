#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    for i in my_list:
        j += 1
        if j <= x:
            print(i ,end="")
        else:
            print("\n" ,end="")
            return j - 1
    print("\n" ,end="")
    return j
