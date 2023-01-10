#!/usr/bin/python3

"""
this module contains one function
this function checks the instance of a
specified class
"""


def is_same_class(obj, a_class):
    """ check instance """
    if type(obj) == a_class:
        return True
    else:
        return False
