#!/usr/bin/python3

"""
function that returns true if the object is an
instance of the class that inherited (directly or indirectly) from the
specified class
"""


def inherits_from(obj, a_class):
    """
    returns true or false
    """
    return type(obj) != a_class and isinstance(obj, a_class)
