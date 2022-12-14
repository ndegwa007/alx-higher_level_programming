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
        if (type(size)) is not int:
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        area func that returns area of Square

        Returns: area
        """
        return self.__size**2
