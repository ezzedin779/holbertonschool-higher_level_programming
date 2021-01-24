#!/usr/bin/python3
""" STUDENT CLASS """


class Student:
    """ Students have first / last name and age """
    def __init__(self, first_name="Unknown", last_name="Unknown", age="0"):
        """ initialise the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ return everything needs to be known """
        return self.__dict__
