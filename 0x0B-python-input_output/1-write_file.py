#!/usr/bin/python3

""" a one function module """


def write_file(filename="", text=""):
    """
    function that writes to a file

    Args:
        filename (str): name of the file
        text (str): text to write to the file
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
