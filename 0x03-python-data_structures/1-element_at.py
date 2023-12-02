#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    elif idx < len(my_list) and idx > 0: 
        return my_list[idx]
