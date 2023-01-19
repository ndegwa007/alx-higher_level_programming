#!/usr/bin/python3
"""This is the rectangle.py unittest module"""
from unittest import TestCase


from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle_basics(TestCase):
    """Test cases for Rectangle initialization"""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_empty(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg_missing(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_Rectangle_only_required(self):
        self.assertEqual(Rectangle(2, 3).id, 1)
        self.assertEqual(Rectangle(4, 5).id, 2)

    def test_Rectangle_width_height_x(self):
        self.assertEqual(Rectangle(1, 2, 3).id, 1)
        self.assertEqual(Rectangle(4, 2, 4).id, 2)

    def test_Rectangle_no_id(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).id, 1)
        self.assertEqual(Rectangle(2, 5, 3, 1).id, 2)

    def test_Rectangle_with_id(self):
        self.assertEqual(Rectangle(2, 3, 4, 5, 6).id, 6)
        self.assertEqual(Rectangle(1, 3, 4, 6, 7).id, 7)

    def test_width_get_set(self):
        r = Rectangle(2, 4, 1, 3)
        with self.assertRaises(AttributeError):
            r.__width
        self.assertEqual(r.width, 2)
        r.width = 5
        self.assertEqual(r.width, 5)

    def test_height_get_set(self):
        r = Rectangle(2, 3, 4, 5)
        with self.assertRaises(AttributeError):
            r.__height
        self.assertEqual(r.height, 3)
        r.height = 10
        self.assertEqual(r.height, 10)

    def test_x_get_set(self):
        r = Rectangle(2, 3, 4, 6)
        with self.assertRaises(AttributeError):
            r.__x
        self.assertEqual(r.x, 4)
        r.x = 3
        self.assertEqual(r.x, 3)

    def test_y_get_set(self):
        r = Rectangle(3, 4, 6, 7)
        with self.assertRaises(AttributeError):
            r.__y
        self.assertEqual(r.y, 7)
        r.y = 2
        self.assertEqual(r.y, 2)

    def test_area(self):
	    r = Rectangle(3, 2)
	    self.assertEqual(r.area(), 6)
	    r.height = 5
	    self.assertEqual(r.area(), 15)
