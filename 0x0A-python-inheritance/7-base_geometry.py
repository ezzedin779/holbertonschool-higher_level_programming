#!/usr/bin/python3
""" Base Geometry Class """


class BaseGeometry:
    """ Base Geometry :) """
    def area(self):
        """ Raise not iplemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Check the VALUE ?"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
