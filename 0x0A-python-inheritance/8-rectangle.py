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
