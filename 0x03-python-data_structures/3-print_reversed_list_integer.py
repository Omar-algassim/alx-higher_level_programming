#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    #my_list.reverse()
    #for i in range(-1,(len(my_list))):
        i = len(my_list) - 1
        while i >= 0:
            print("{}".format(my_list[i]))
            i -= 1
