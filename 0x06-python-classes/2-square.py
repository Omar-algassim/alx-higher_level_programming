#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    pass

    def __init__(self, size=0):

        """Defin the metod of square and most be integer"""
        self.__size = size
        try:
            isinstance(size, int)
        except TypeError:
            print("size must be an integer")
        try:
            size < 0
        except ValueError:
            print("size must be >= 0")