#!/usr/bin/python3
""" Defining a Square class contains The size ? """


class Square:
    """ New item SIZEEEE """
    def __init__(self, size=0):
        """ Initialize the size ? please ?
        Do verification also please"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Calculate the area """
        return self.__size * self.__size
