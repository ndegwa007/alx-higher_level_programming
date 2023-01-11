#!/usr/bin/python3

""" a module with a BaseGeometry class """


class BaseGeometry(object):
    """ a public instance method """
    def area(self):
        """ empty method """
        raise Exception("area() is not implemented")

    """ integer validator """
    def integer_validator(self, name, value):
        """
        integer validator

        Args:
            name (string): a string
            value (int): the integer value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        
        self.name = name
        self.value = value
