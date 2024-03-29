#!/usr/bin/python3

"""
a class method that prevents dynamic attribute creation
"""


class LockedClass():
    """prevents dynamic allocation"""
    __slots__ = ['first_name']

    def __init__(self):
        """init method without attributes"""
        pass
