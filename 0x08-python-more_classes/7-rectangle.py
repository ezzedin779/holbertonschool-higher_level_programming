#!/usr/bin/python3
""" Creating a new Rectangle """


class Rectangle:
    """ upgraded rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initialize my Rectangle"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ retrieving the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width value ??"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieving the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the height value ??"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculate the Area ?"""
        return self.__width * self.__height

    def perimeter(self):
        """ Calculate the Perimeter ?"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2*(self.__height + self.__width)

    def __str__(self):
        """ printing the rectangle ??"""
        rect = ""
        if self.__height == 0 or self.__width == 0:
            return rect
        for i in range(self.__height):
            for j in range(self.width):
                rect += str(self.print_symbol)
            if i < self.__height:
                rect += "\n"
        return rect

    def __repr__(self):
        """ Eval Magic ? """
        rect = "Rectangle(" + str(self.width) + "," + str(self.height) + ")"
        return rect

    def __del__(self):
        """ DELETED """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
