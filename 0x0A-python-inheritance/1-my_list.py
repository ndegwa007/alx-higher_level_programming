#!/usr/bin/python3

"""
module with a class that inherits from a list class
"""


class MyList(list):
    """
    prints a sorted list
    """
    def print_sorted(self):
        """
        printing the sorted list
        """
        print(sorted(self))
