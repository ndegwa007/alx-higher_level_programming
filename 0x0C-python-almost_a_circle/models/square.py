#!/usr/bin/python3
""" this is a square module """
from models.rectangle import Rectangle
""" importing Rectangle object class  """


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

    @property
    def size(self):
        """ gets the value of object self.size after being set """
        return self.width

    @size.setter
    def size(self, value):
        """ validates then sets the size """

        if type(self.width) is not int:
            raise("[TypeError] width must be an integer")
        self.width = value
        self.height = value
