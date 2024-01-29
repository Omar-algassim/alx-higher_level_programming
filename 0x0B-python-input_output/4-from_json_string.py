#!/usr/bin/python3
""" load json file """
import json

def from_json_string(my_str):
    """load json to python

    Args:
        my_str (str): string in json
    """
    return json.loads(my_str)
