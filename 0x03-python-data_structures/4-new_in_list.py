#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp = my_list.copy()

    if idx < 0 or (len(my_list) - 1) < idx:
        return cp
    else:
        cp[idx] = element
        return cp    