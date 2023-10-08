def new_in_list(my_list, idx, element):
    copy_l = my_list.copy()
    if idx < 0 or idx >= len(copy_l):
        return copy_l
    copy_l[idx] = element
    return copy_l
