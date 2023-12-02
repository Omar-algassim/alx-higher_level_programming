#!/usr/bin/python3
def no_c(my_string):
    remove = ['c', 'C']
    plc = my_string.replace('c', ' ')
    plc = plc.replace('C', ' ')
    return plc