#!/usr/bin/python3

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_init(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertIsNone(s1.id:)

        s2 = Square(2, 2, 2, 12)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 2)
        self.assertEqual(s2.id, 12)

    def test_area(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

        s2 = Square(2)
        self.assertEqual(s2.area(), 4)

    def test_str(self):
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (5) 0/0 - 5")

        s2 = Square(2, 2, 2, 12)
        self.assertEqual(str(s2), "[Square] (12) 2/2 - 2")
