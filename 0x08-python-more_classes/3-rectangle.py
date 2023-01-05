#!/usr/bin/python3

"""
This is a 0-rectangle module
The module contains a class with width and height attributes
"""


class Rectangle:

    """class defines the rectangle dimensions"""

    def __init__(self, width=0, height=0):
        """ instance method """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ getter method """
        return self.__width

    @width.setter
    def width(self, width):
        """ setter method """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

        self.__width = width

    @property
    def height(self):
        """ getter method """
        return self.__height

    @height.setter
    def height(self, height):
        """ setter method """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height

    def area(self):
        """ returns rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ returns rectangle perimeter """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        return printable representation of the rectangle
        represents the rectangle with "#" character
        """

        if self.__height == 0 or self.__width == 0:
            return ""

        rect = []
        i = 0
        while(i < self.__height):
            [rect.append("#") for j in range(self.__width)]
            if (i != self.__height - 1):
                rect.append("\n")
            i += 1
        return "".join(rect)
