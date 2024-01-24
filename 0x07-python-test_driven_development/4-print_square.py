#!/usr/bin/python3
"""define print square"""


def print_square(size):
    """function that prints a square with the character #
    
    Args:
        size (int): is the size length of the square
    Raises:
        TypeError: size must be an integer
        ValueError: if size is less than 0
        TypeError: if size is a float and is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) or size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
