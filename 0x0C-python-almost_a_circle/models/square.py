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
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__width = value
        self.__height = value
        
    def __str__(self):
        ret = "[{}] ({}) ".format(str(self.__class__.__name__), self.id)
        ret += "{}/{} - {}".format(self.x, self.y, self.__size)
        return ret
    
    def update(self, *args, **kwargs):
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
        return {'id': self.id, 'x': self.x, 'size': self.__size, 'y': self.y}
