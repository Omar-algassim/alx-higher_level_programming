#!/usr/bin/python3
""" inherite class from base geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle base on height and width """

    def __init__(self, width, height):
        """height and width """
        super().integer_validator("height", height)
        self.__height = height
        super().integer_validator("width", width)
        self.__width = width

    def area(self):
        """return the area of Rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """ print Rectangle formate """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
