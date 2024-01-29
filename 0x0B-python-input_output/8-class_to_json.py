#!/usr/bin/python3
"""define class to json"""


def class_to_json(obj):
    """return a dictntoiinry

    Args:
        obj (instance): is an instance of a Class
    """
    return obj.__dict__
