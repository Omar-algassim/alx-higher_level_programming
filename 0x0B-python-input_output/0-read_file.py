#!/usr/bin/python3
"""define the read file"""


def read_file(filename=""):
    """read file and print in stdout

    Args:
        filename (str): the name of file. Defaults to "".
    """
    with open(filename, encoding="utf-8") as f:
        data = f.read()
        print(data)
