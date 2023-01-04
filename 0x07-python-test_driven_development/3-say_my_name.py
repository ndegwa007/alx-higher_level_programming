#!/usr/bin/python3

"""
say_my_name module
This module returns first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Returns first and last name

    Args:
        first_name(string): first name
        last_name(string): last name
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
