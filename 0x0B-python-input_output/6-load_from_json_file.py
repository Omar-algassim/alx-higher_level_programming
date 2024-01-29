#!/usr/bin/python3
"""define load json to file"""
import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file

    Args:
        filename (file): json file will read from
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)