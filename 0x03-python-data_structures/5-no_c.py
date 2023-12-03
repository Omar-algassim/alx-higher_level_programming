#!/usr/bin/python3
def no_c(my_string):
    plc = ""
    for char in my_string:
        if char == 'c' or char == 'C':
            plc += ''
        else:
            plc += char
    return plc
