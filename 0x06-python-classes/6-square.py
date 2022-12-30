#!/usr/bin/python3
""" a class raising errors and gets the area of square"""


class Square:

    """ a square class that defines a square """
    def __init__(self, size=0, position=(0, 0)):
        """
        initialize obj in Square
        Args:
            size(int): size of the square
            position(int, int): tuple
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        get position value
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value)) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        area func that returns area of Square

        Returns: area
        """
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print()
        for j in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
