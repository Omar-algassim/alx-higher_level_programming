#!/usr/bin/python3
"""define the json to file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Args:
        my_obj (obj): object will writ in file
        filename (file):a file will write in
    """
    with open(filename, 'w', encoding='utf-8') as f:
        file_write = json.dumps(my_obj)
        f.write(file_write)
