#!/usr/bin/python3

from models.rectangle import Rectangle
""" this is a square module """


class Square(Rectangle):

    """ This square class that inherits from Rectangle class and defines a
    Square object"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        initialize the default attribute of the base object.
        Args:
            size (int): the size of a square side
            x (int): the wanted horizontal (x) padding of the square
            y (int): the wanted vertical (y) padding of the square
            id (int): the wanted identifier of the Base object.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overwrites the __str__ method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
