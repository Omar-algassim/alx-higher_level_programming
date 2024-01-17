#!/usr/bin/python3
"""test for recatangle"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class testRectangle(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""
    
    def test_setter(self):
        """test the value set for recatangle"""
        r1 = Rectangle(10, 10, 5, 5, 0)
        r1.width = 3
        self.assertEqual(r1.width, 3)
        r1.height = 1
        self.assertEqual(r1.height, 1)
        r1.x = 2
        self.assertEqual(r1.x, 2)
        r1.y = 3
        self.assertEqual(r1.y, 3)
        with self.assertRaises(ValueError):
            r1.width = 0
        with self.assertRaises(ValueError):
            r1.height = 0
        with self.assertRaises(ValueError):
            r1.x = -1
        with self.assertRaises(ValueError):
            r1.y = -1
        with self.assertRaises(TypeError):
            r1.width = "0"
        with self.assertRaises(TypeError):
            r1.height = "0"        
        with self.assertRaises(TypeError):
            r1.x = "0"
        with self.assertRaises(TypeError):
            r1.y = "0"
        
    def test_rectangle_is_base(self):
        """is it base"""
        self.assertIsInstance(Rectangle(10, 2), Base)
    
    def test_area(self):
        """test the area method"""
        a1 = Rectangle(5, 3)
        self.assertEqual(a1.area(), 15)
        
    def test_dispplay(self):
        """test display method"""
        d1 = Rectangle(1, 2, 1, 1)