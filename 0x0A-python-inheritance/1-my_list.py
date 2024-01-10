#!/usr/bin/python3
""" define the MyList """


class MyList(list):
    """ subclass from list"""
    def __init__(self):
        """ initialze the object """
        super().__init__()
    def print_sorted(self):
        """ print the sorted """
        print(sorted(self))

