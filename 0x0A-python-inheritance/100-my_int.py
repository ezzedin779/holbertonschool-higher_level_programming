#!/usr/bin/python3
""" MyInt Class """


class MyInt(int):
    """ The Inverted Class got int """
    def __eq__(self, value):
        """ invert the equality """
        return self.real != value

    def __ne__(self, value):
        """ invert the not equal """
        return self.real == value
