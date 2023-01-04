#!/usr/bin/python3

"""
this is a 4-print_square module
this module has one function
"""


def print_square(size):
    """
    print a square with the character #

    Args:
        size(int): size length of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    i = 0
    while(i < size):
        print(size * "#")
        i += 1
