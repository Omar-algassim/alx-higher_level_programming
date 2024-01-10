#!/usr/bin/python3
""" define a BaseGeometry class"""


class BaseGeometry:
    """empty class"""
    pass

    def area(self):
        """ raise Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate the value """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
