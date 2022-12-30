#!/usr/bin/python3
""" a class raising errors and gets the area of square"""


class Square:

    """ a square class that defines a square """
    def __init__(self, size=0):
        """
        initialize obj in Square
        Args:
            size(int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """
        get size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set size value
        """
        if (type(value)) is not int:
            raise TypeError("size must be an integer")
        elif(value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        area func that returns area of Square

        Returns: area
        """
        return self.__size**2
