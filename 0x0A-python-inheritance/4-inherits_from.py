#!/usr/bin/python3
""" subcalsses only """


def inherits_from(obj, a_class):
    """ return true if object is directly or indirectly
    inherite from class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
