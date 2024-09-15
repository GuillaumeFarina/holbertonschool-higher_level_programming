#!/usr/bin/python3
"""Unittest for max_integer([..]
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_int(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_floats(self):
        self.assertEqual(max_integer([1.2, 2.2, 3.2, 4.2]), 4.2)
    
    def test_string(self):
        self.assertEqual(max_integer("string"), 't')

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
    
    def test_value(self):
        self.assertRaises(TypeError, max_integer, ['6', 5])