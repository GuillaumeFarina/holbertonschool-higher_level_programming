#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """
    A class that defines a student by first name, last name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Student instance.
        """
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute names
        contained in this list are retrieved.
        Otherwise, all attributes are retrieved.
        """
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for index in attrs:
            if index in self.__dict__:
                new_dict[index] = self.__dict__[index]
        return new_dict