#!/usr/bin/python3

""" a module with one function """


def read_file(filename=""):
    """
    read_file: function that reads a file
    Args:
        filename (str): file name
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
