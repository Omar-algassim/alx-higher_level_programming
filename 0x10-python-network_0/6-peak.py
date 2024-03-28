#!/usr/bin/python3
"""define method find the maximum of integer"""


def find_peak(list_of_integers):
    """find the peak of the list"""
    if len(list_of_integers) > 0:
        return max(list_of_integers)
