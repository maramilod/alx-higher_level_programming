def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    copy_l = my_list.copy()
    copy_l[idx] = element
    return copy_l
