#!/usr/bin/python3
"""test for Base"""
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class testBase(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""
    
    def test_type_of_Base(self):
        """test if is class or not"""
        obj = Base()
        self.assertIsInstance(obj, Base)

    def test_id(self):
        """test if id increas if it is None"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(10)
        self.assertEqual(b2.id, 10)
        b3 = Base(-10)
        self.assertEqual(b3.id, -10)
        b4 = Base(0)
        self.assertEqual(b4.id, 0)
        b5 = Base(10)
        self.assertIsInstance(b5.id, int)
    
    def test_to_json_string(self):
        """test for json string method"""
        dic = {'x': 1, 'y': 2}
        json_out = json.dumps(dic)
        fun_out = Base().to_json_string(dic) 
        self.assertEqual(json_out, fun_out)
    
    def test_save_to_file(self):
        """ test save t fille"""
        r1 = Rectangle(5, 10, 6)
        r2 = Rectangle(3, 6, 1, 2)
        Base.save_to_file([r1, r2])
        with open("Rectangle.json", 'r', encoding='utf-8') as f:
            self.assertIsInstance(f.read(), str)
    
    def test_from_json_string(self):
        """test from_json_string method"""
        json_str = '[{"x": 2, "y":3}, {"o": 5, "p": 9}]'
        py_list = json.loads(json_str)
        py_list1 = Base.from_json_string(json_str)
        self.assertEqual(py_list, py_list1)
        json_str = None
        py_list = Base.from_json_string(json_str)
        self.assertEqual(py_list, [])
    
    def test_create(self):
        """test the creat method"""
        r1 = Rectangle(3, 5, 1, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)
    