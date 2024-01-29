#!/usr/bin/python3
"""define Student class"""


class Student:
    """student calss"""

    def __init__(self, first_name, last_name, age):
        """initilize new student

        Args:
            first_name (str): the first name of student
            last_name (str): the last name of student
            age (int): the student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """class to json"""
        return self.__dict__
