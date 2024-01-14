#!/usr/bin/python3
""" define writing in file """


def write_file(filename="", text=""):
    """ write in file and creat it if doesnt exist"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
