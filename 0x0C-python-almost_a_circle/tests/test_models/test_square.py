#!/usr/bin/python3

import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Test cases for Square initialization."""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_empty(self):
        with self.assertRaises(TypeError):
            Square()

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_Square_only_required(self):
        self.assertEqual(Square(2).id, 1)
        self.assertEqual(Square(4).id, 2)

    def test_Square_size_x(self):
        self.assertEqual(Square(2, 1).id, 1)
        self.assertEqual(Square(4, 2).id, 2)

    def test_Square_no_id(self):
        self.assertEqual(Square(2, 1, 2).id, 1)
        self.assertEqual(Square(4, 2, 1).id, 2)

    def test_Square_with_id(self):
        self.assertEqual(Square(2, 1, 2, 4).id, 4)
        self.assertEqual(Square(4, 2, 1, 2).id, 2)

    def test_size_get_set(self):
        s = Square(2, 1, 2)
        self.assertEqual(s.size, 2)
        s.size = 42
        self.assertEqual(s.size, 42)

    def test_width_get(self):
        s = Square(2, 1, 2)
        self.assertEqual(s.width, 2)

    def test_height_get(self):
        s = Square(2, 1, 2)
        self.assertEqual(s.height, 2)

    def test_x_get(self):
        s = Square(2, 1, 2)
        self.assertEqual(s.x, 1)

    def test_y_get(self):
        s = Square(2, 1, 2)
        self.assertEqual(s.y, 2)
