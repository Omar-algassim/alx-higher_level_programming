#!/usr/bin/python3
""" define append in file """


def append_write(filename="", text=""):
    """ append text in file and creat it if doesnt exist"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
