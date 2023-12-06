#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set(my_list)
    ret = 0
    for i in uniq:
        ret += i
    return ret
