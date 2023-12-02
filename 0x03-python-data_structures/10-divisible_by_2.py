#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ret = []
    length = len(my_list)
    i = 0
    while i < (length):
        if (my_list[i] % 2) == 0:
            ret.append(True)
        else:
            ret.append(False)
        i += 1
    return ret
