#!/usr/bin/python3
""" define the square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class inhert from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """ squre argument and id """
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        """the getter/setter of size"""
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value
        self.height = value

    def __str__(self):
        """return the string of instaces

        Returns:
            str: the instances
        """
        ret = "[{}] ({}) ".format(str(self.__class__.__name__), self.id)
        ret += "{}/{} - {}".format(self.x, self.y, self.__size)
        return ret

    def update(self, *args, **kwargs):
        """update the instance of attribute"""
        if args:
            argu = []
            for arg in args:
                argu.append(arg)
            if len(argu) > 0:
                self.id = argu[0]
            if len(argu) > 1:
                self.__size = argu[1]
            if len(argu) > 2:
                self.x = argu[2]
            if len(argu) > 3:
                self.y = argu[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.__size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """transfer the instance to dictionary

        Returns:
            dict: the instance of attribute
        """
        return {'id': self.id, 'x': self.x, 'size': self.__size, 'y': self.y}
