#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    pass

    def __init__(self, size=0):

        """Defin the metod of square and most be integer"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
