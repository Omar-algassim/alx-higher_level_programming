"""test for recatangle"""
import unittest
from models.base import Base
from models.square import Square
import io
import sys

class testSquare(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""
    
    @staticmethod
    def capture_stdout(sq, method):
        """Captures and returns text printed to stdout.

        Args:
            sq (Square): The Square ot print to stdout.
            method (str): The method to run on sq.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_setter(self):
        """test the value set for recatangle"""
        r1 = Square(10, 5, 5, 0)
        r1.size = 3
        self.assertEqual(r1.size, 3)
        r1.size = 1
        self.assertEqual(r1.size, 1)
        r1.x = 2
        self.assertEqual(r1.x, 2)
        r1.y = 3
        self.assertEqual(r1.y, 3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.size = 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.size = 0
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.x = -1
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.y = -1
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.size = "0"
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.size = "0"        
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.x = "0"
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.y = "0"
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.size = float('inf')
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.size = float('inf')     
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.x = float('inf')
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.y = float('inf')
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.size = [1, 2, 3]
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.size = [1, 2, 3]    
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.x = [1, 2, 3]
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.y = [1, 2, 3]

    def test_Square_is_base(self):
        """is it base"""
        self.assertIsInstance(Square(10, 2), Base)
    
    def test_area(self):
        """test the area method"""
        a1 = Square(5)
        self.assertEqual(a1.area(), 25)
        a2 = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            a2.area(1)

    def test_dispplay(self):
        """test display method"""
        d1 = Square(1, 0, 0, 0)
        capture = testSquare.capture_stdout(d1, "display")
        self.assertEqual(capture.getvalue(), "#\n")
        d2 = Square(2, 3, 4, 5)
        capture1 = testSquare.capture_stdout(d2, "display")
        expected_output = (
            "\n\n\n\n"
            "   ##\n"
            "   ##\n"
        )
        self.assertEqual(capture1.getvalue(), expected_output)
        d2 = Square(4, 3, 0, 0)
        capture1 = testSquare.capture_stdout(d2, "display")
        expected_output = (
            "   ####\n"
            "   ####\n"
            "   ####\n"
            "   ####\n"
        )
        self.assertEqual(capture1.getvalue(), expected_output)
        d2 = Square(3, 3, 1, 0)
        capture1 = testSquare.capture_stdout(d2, "display")
        expected_output = (
            "\n"
            "   ###\n"
            "   ###\n"
            "   ###\n"
        )
        self.assertEqual(capture1.getvalue(), expected_output)
        d2 = Square(2, 3, 0, 1)
        capture1 = testSquare.capture_stdout(d2, "display")
        expected_output = (
            "   ##\n"
            "   ##\n"
        )
        self.assertEqual(capture1.getvalue(), expected_output)

    def test_print(self):
        p1 = Square(6, 2, 1, 0)
        capture1 = testSquare.capture_stdout(p1, "print")
        expected_output = ("[Square] (0) 2/1 - 6\n")
        self.assertEqual(capture1.getvalue(), expected_output)
        p2 = Square(5, 5, 1)
        capture1 = testSquare.capture_stdout(p2, "print")
        expected_output = ("[Square] (23) 5/1 - 5\n")
        self.assertEqual(capture1.getvalue(), expected_output)
        p3 = Square(1, 1)
        capture1 = testSquare.capture_stdout(p3, "print")
        expected_output = ("[Square] (24) 1/0 - 1\n")
        self.assertEqual(capture1.getvalue(), expected_output)

    def test_update(self):
        r1 = Square(10, 10, 10)
        r2 = Square(3, 3, 4, 89) 
        r1.update(89)
        self.assertEqual(r1.id, r2.id)
        r1.update(89, 3)
        self.assertEqual(r1.size, r2.size)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, r2.x)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, r2.y)

    def test_dictionary(self):
        r1 = Square(10, 10, 10, 10)
        expected_output = {'y': 10, 'x': 10, 'id': 10, 'size': 10}
        self.assertEqual(r1.to_dictionary(), expected_output)
        r1 = Square(10)
        expected_output = {'y': 0, 'x': 0, 'id': 22, 'size': 10}
        self.assertEqual(r1.to_dictionary(), expected_output)