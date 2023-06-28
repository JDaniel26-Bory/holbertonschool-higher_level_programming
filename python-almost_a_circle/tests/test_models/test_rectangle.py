#!/usr/bin/python3
"""Unittests for Rectangle class
"""


from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class
    """
    def setUp(self):
        """assigning automatically an ID + 1 of the previous"""
        Base._Base__nb_objects = 0

    def test_A_entry_normal_values(self):
        """test to check entry values for a Rectangle
        """
        rectangle1 = Rectangle(1, 2)
        self.assertEqual(rectangle1.id, 1)
        self.assertEqual(rectangle1.width, 1)
        self.assertEqual(rectangle1.height, 2)

        rectangle2 = Rectangle(1, 2, 3)
        self.assertEqual(rectangle2.id, 2)
        self.assertEqual(rectangle2.width, 1)
        self.assertEqual(rectangle2.height, 2)
        self.assertEqual(rectangle2.x, 3)

        rectangle3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rectangle3.id, 3)
        self.assertEqual(rectangle3.width, 1)
        self.assertEqual(rectangle3.height, 2)
        self.assertEqual(rectangle3.x, 3)
        self.assertEqual(rectangle3.y, 4)

    def test_A_entry_wrong_values(self):
        """test to check entry values for a Rectangle
        """
        with self.assertRaises(ValueError):
            r = Rectangle("1", 2)

        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")

        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "3")

        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "4")
        
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)
        
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)
        
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3)
        
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4)
        
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3 , 4, 5)

if __name__ == '__main__':
    unittest.main()