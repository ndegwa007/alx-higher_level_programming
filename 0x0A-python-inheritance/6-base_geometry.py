#!/usr/bin/python3

""" a module with a BaseGeometry class """


class BaseGeometry(object):
    """ a class with one method """
    def area(self):
        """ empty method """
        raise Exception("area() is not implemented")
