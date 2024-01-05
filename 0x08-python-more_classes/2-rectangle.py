#!/usr/bin/python3
"""define rectangle"""


class Rectangle:

    """ the rectangle """

    def __init__(self, width=0, height=0):

        """ width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ret = 0.5 * self.width * self.height
        return ret
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            ret = 0
        else:
            ret = 2 * (self.width + self.height)
        return ret