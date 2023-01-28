#!/usr/bin/python3

from models.rectangle import Rectangle
""" this is a square module """


class Square(Rectangle):

    """ a square class that inherits from Rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialize the class """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overwrites the str method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
