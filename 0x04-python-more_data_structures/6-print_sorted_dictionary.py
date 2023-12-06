#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list(a_dictionary)
    sortset = sorted(a_dictionary)
    for i in sortset:
        print("{}: {}".format(i, a_dictionary[i]))
