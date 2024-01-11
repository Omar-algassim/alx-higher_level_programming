#!/usr/bin/python3
""" define integer addition function """


def add_integer(a, b=98):
    """add tow integer number a and b 

    Args:
        a (int): the first number
        b (int): the second number. Defaults to 98.

    Raises:
        TypeError: 
      

    Returns:
        int : the result of add
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    ret = int(a) + int(b)
    return ret