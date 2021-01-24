#!/usr/bin/python3
""" New things in Base Geometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectange is in base geometry"""
    def __init__(self, width, height):
        """ Validate the passed values ?"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Simple Area ?"""
        return self.__width * self.__height

    def __str__(self):
        """ STR() && PRINT() """
        s = "[" + str(self.__class__.__name__) + "] " + str(self.__width)
        s += "/" + str(self.__height)
        return s
