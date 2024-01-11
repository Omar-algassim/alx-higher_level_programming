#!/usr/bin/python3
""" define subclass saure from rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """squre class froem Rectangle"""

    def __init__(self, size):
        """ size of squre"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
