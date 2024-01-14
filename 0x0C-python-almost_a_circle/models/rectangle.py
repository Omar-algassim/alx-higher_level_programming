#!/usr/bin/python3
""" define Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Rectangle inherite from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """define the height and width

        Args:
            width (int): width of rectabgle
            height (int): height of rectangle
            x (int): the x of rectangle. Defaults to 0.
            y (int): the y of recatangle. Defaults to 0.
            id (int): the id of base. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def display(self):
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        ret = "[{}] ({}) ".format(str(self.__class__.__name__), self.id)
        ret += "{}/{}".format(self.__x, self.__y,)
        ret += " - {}/{}".format(self.__width, self.__height)
        return ret

    def update(self, *args, **kwargs):
        if args:
            argu = []
            for arg in args:
                argu.append(arg)
            if len(argu) > 0:
                self.id = argu[0]
            if len(argu) > 1:
                self.__width = argu[1]
            if len(argu) > 2:
                self.__height = argu[2]
            if len(argu) > 3:
                self.__x = argu[3]
            if len(argu) > 4:
                self.__y = argu[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """return dectionary """
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
