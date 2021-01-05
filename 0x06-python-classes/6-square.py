#!/usr/bin/python3
""" Defining a Square class contains The size ? """


class Square:
    """ New item SIZEEEE """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize the size ? please ?
        Do verification also please"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """get the position ?"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position"""
        if type(value) == tuple and len(value) == 2 and \
           type(value[0]) == int and value[0] >= 0 and \
           type(value[1]) == int and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Calculate the area """
        return self.__size * self.__size

    def my_print(self):
        """ Printing the square """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print("")
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print("")
