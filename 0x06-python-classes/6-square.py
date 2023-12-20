#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""


    def __init__(self, size=0, position=(0, 0)):

        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @position.setter
    def position(self, value):
        if (position[0] < 0 or
                len(value) != 2 or
                position[1] < 0 or
                not isinstance(position[0], int) or
                not isinstance(position[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):

        """return the squre area"""

        return self.__size ** 2

    def my_print(self):

        """print the square as a (#)"""


        if self.__size == 0:
            print("")
        else:
            if self.__position[1] > 0:
                for p in range(self.__position[1]):
                    print("")
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
