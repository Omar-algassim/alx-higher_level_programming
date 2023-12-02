#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    new_list = my_list
    if 0 > idx or (len(my_list)) - 1 < idx:
        return my_list
    elif (len(my_list)) > idx:
        new_list[idx] = element
        return new_list
    