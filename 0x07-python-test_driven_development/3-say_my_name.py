#!/usr/bin/python3
"""define say my name"""


def say_my_name(first_name, last_name=""):
    """function that prints My name is <first name> <last name>

    Args:
        first_name (str): first name
        last_name (str, optional): last name. Defaults to "".

    Raises:
        TypeError: first_name and last_name must be strings
        TypeError: first_name and last_name must be strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
