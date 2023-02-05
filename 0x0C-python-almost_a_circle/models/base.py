#!/usr/bin/python3
""" This is the Base module.
Contains the Base class which will be the
"base" of all other classes in this project
"""


class Base():
    """ This class will be the "base" of all other classes in this
    project. The goal is to manage id attribute in all our future classes
    and to avoid duplicating the same code and same errors.
    Attributes:
        __nb_objects (int): the number of created Base objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes the default attributes of the Base object
        Args:
            id(int): the identifier of the Base object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
