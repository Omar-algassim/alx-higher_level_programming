#!/usr/bin/python3
"""test for recatangle"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
import sys

class testRectangle(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""
    
    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout.

        Args:
            sq (Rectangle): The Rectangle ot print to stdout.
            method (str): The method to run on sq.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

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
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.width = 0
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.height = 0
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.x = -1
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.y = -1
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.width = "0"
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.height = "0"        
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.x = "0"
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.y = "0"
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.width = float('inf')
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.height = float('inf')     
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.x = float('inf')
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.y = float('inf')
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.width = [1, 2, 3]
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.height = [1, 2, 3]    
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.x = [1, 2, 3]
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.y = [1, 2, 3]

    def test_rectangle_is_base(self):
        """is it base"""
        self.assertIsInstance(Rectangle(10, 2), Base)
    
    def test_area(self):
        """test the area method"""
        a1 = Rectangle(5, 3)
        self.assertEqual(a1.area(), 15)
        a2 = Rectangle(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            a2.area(1)

    def test_dispplay(self):
        """test display method"""
        d1 = Rectangle(1, 1, 0, 0)
        capture = testRectangle.capture_stdout(d1, "display")
        self.assertEqual(capture.getvalue(), "#\n")
        d2 = Rectangle(2, 3, 4, 5)
        capture1 = testRectangle.capture_stdout(d2, "display")
        expected_output = (
            "\n\n\n\n\n"
            "    ##\n"
            "    ##\n"
            "    ##\n"
        )
        self.assertEqual(capture1.getvalue(), expected_output)
        d2 = Rectangle(2, 3, 0, 0)
        capture1 = testRectangle.capture_stdout(d2, "display")
        expected_output = (
            "##\n"
            "##\n"
            "##\n"
        )
        self.assertEqual(capture1.getvalue(), expected_output)
        d2 = Rectangle(2, 3, 1, 0)
        capture1 = testRectangle.capture_stdout(d2, "display")
        expected_output = (
            " ##\n"
            " ##\n"
            " ##\n"
        )
        self.assertEqual(capture1.getvalue(), expected_output)
        d2 = Rectangle(2, 3, 0, 1)
        capture1 = testRectangle.capture_stdout(d2, "display")
        expected_output = (
            "\n"
            "##\n"
            "##\n"
            "##\n"
        )
        self.assertEqual(capture1.getvalue(), expected_output)

    def test_print(self):
        p1 = Rectangle(4, 6, 2, 1, 0)
        capture1 = testRectangle.capture_stdout(p1, "print")
        expected_output = ("[Rectangle] (0) 2/1 - 4/6\n")
        self.assertEqual(capture1.getvalue(), expected_output)
        p2 = Rectangle(5, 5, 1)
        capture1 = testRectangle.capture_stdout(p2, "print")
        expected_output = ("[Rectangle] (15) 1/0 - 5/5\n")
        self.assertEqual(capture1.getvalue(), expected_output)
        p3 = Rectangle(1, 1)
        capture1 = testRectangle.capture_stdout(p3, "print")
        expected_output = ("[Rectangle] (16) 0/0 - 1/1\n")
        self.assertEqual(capture1.getvalue(), expected_output)

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r2 = Rectangle(2, 3, 4, 5, 89) 
        r1.update(89)
        self.assertEqual(r1.id, r2.id)
        r1.update(89, 2)
        self.assertEqual(r1.width, r2.width)
        r1.update(89, 2, 3)
        self.assertEqual(r1.height, r2.height)
        r1.update(89, 2, 3, 4) 
        self.assertEqual(r1.x, r2.x)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, r2.y)