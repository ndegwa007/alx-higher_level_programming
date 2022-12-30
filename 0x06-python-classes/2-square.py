#!/usr/bin/python3
""" a class that raises errors """


class Square:
    """
    a Square class that defines a square

    Args:
        size(int): integer size of a square
    """
    def __init__(self, size=0):

        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
