#!/usr/bin/python3
"""define base class """
import json


class Base:
    """the base class of all classess"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ define id and increament it if it not None

        Args:
            id (int) the value will be manage it . Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ that returns the JSON string representation of
        list_dictionaries

        Args:
            list_dictionaries (dict): dictionary of values
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class mehtod save the dictionry in json file

        Args:
            list_objs (list): objects of inherits classes
        """
        ret = []
        if list_objs is not None:
            filename = "{}.json".format(str(cls.__name__))
            with open(filename, "w", encoding="utf-8") as f:
                if list_objs is None:
                    f.wirte([])
                else:
                    dic = [obj.to_dictionary() for obj in list_objs]
                    wr = Base.to_json_string(dic)
                    f.write(wr)

    @staticmethod
    def from_json_string(json_string):
        """re that returns the list of the
        JSON string representation json_string:

        Args:
            json_string (str): is a string representing a list of dictionaries
        """
        if json_string is None or json == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create instance and return with

        Returns:
            instance: new istance with new argument
        """
        inst = cls(0, 0)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """load string from json file

        Returns:
            list: a list of instance
        """
        try:
            filename = "{}.json".format(cls.__name__)
            with open(filename, "r", encoding="utf-8") as f:
                file_ = f.read()
                dic = Base.from_json_string(file_)
                return [cls.create(**i) for i in dic]
        except FileNotFoundError:
            return []
