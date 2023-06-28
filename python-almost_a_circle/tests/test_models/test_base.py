#!/usr/bin/python3
"""Unittests for Base class
"""


from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """Test cases for Base class
    """
    def setUp(self):
        """assigning automatically an ID + 1 of the previous"""
        Base._Base__nb_objects = 0

    def test_A_ID_value(self):
        """tests for class base differente instances
        """
        base1 = Base()
        base2 = Base()
        base3 = Base()

        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)
    
    def test_id_generation(self):
        """Base(89) saving the ID passed"""
        base1 = Base()
        base2 = Base(89)

        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 89)

if __name__ == '__main__':
    unittest.main()