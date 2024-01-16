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
        
    def test_rectangle_is_base(self):
        """is it base"""
        self.assertIsInstance(Rectangle(10, 2), Base)
    