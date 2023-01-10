#!/usr/bin/python3

""" one function module """


def append_write(filename="", text=""):
    """
    append_write: a function that appends
    a string at the end of a text file

    Args:
        filename (str): filename
        text (str): string to append
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
