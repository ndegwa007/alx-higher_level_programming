#!/usr/bin/python3
"""This is the base.py unittest module"""
from unittest import TestCase


from models.base import Base


class Test_Base_ID(TestCase):
    """Test cases for Base id."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_ID_empty(self):
        self.assertEqual(Base().id, 1)

    def test_ID_none(self):
        self.assertEqual(Base(None).id, 1)

    def test_ID_positive(self):
        self.assertEqual(Base(10).id, 10)

    def test_ID_negative(self):
        self.assertEqual(Base(-20).id, -20)

    def test_ID_mixed(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(None).id, 2)
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base(None).id, 4)
        self.assertEqual(Base(-35).id, -35)

if __name__ == "__main__":
    unittest.main()
