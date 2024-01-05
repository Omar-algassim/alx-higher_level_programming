#!/usr/bin/python3
"""define rectangle"""


class Rectangle:

    """ the rectangle """
    pass
def __init__(self, width):
    
    """ width of triangle """
    if width < 0:
        raise ValueError("width must be >= 0")
    if not isinstance(int, width):
        raise TypeError("width must be an integer")
    self.__width = width

@property
def width(self):
    return self.__width

@width.setter
def width(self, value):
    if width < 0:
        raise ValueError("width must be >= 0")
    if not isinstance(width, int):
        raise TypeError("width must be an integer")
    self.__width = value

def __init__(self, height):
    
    """ heigh of triangle """
    if height < 0:
        raise ValueError("width must be >= 0")
    if not isinstance(height, int):
        raise TypeError("width must be an integer")
    self.__height = height
@property
def height(self):
    return self.__height

@height.setter
def height(self, value):
    if height < 0:
        raise ValueError("height must be >= 0")
    if not isinstance(height, int):
        raise TypeError("height must be an integer")
    self.__height = value

def __init__(self, width=0, height=0):
    
    """ width and height """
    self.width = width
    self.height = height