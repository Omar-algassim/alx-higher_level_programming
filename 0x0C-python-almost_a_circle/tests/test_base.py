#!/usr/bin/python3
"""test for Base"""
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class testBase(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""
    
    def test_id(self):
        """test if id increas if it is None"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(10)
        self.assertEqual(b2.id, 10)
        b3 = Base(10)
        self.assertIsInstance(b3.id, int)
    
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
        
            