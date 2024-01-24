#!/usr/bin/python3
"""define the indention function"""


def text_indentation(text):
    """indentation for string

    Args:
        text (str): the text will indent
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        print(i, end="")
        if i == ":" or i == "." or i == "?":
            print("\n")
            