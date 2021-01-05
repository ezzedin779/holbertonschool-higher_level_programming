#!/usr/bin/python3
""" Defining a Square class contains The size ? """


class Square:
    """ New item SIZEEEE """

    def __init__(self, size=0):
        """ Initialize the size ? please ?
        Do verification also please"""
        self.size = size

    @property
    def size(self):
        """ Retrieving it ?"""
        return self.__size

    @size.setter
    def size(self, nsize):
        """ Setting the Mine ?"""
        if type(nsize) != int:
            raise TypeError("size must be an integer")
        elif nsize < 0:
            raise ValueError("size must be >= 0")
        self.__size = nsize

    def area(self):
        """ Calculate the area """
        return self.__size * self.__size

    def my_print(self):
        """ Printing the square """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
