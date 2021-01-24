#!/usr/bin/python3
""" New THINGS IN GEOMETRY"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A SQUARE """
    def __init__(self, size):
        """ initialise my square """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
