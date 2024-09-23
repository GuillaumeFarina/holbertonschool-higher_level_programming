#!/usr/bin/python3
"""
This is a docstring for the module.
"""


class BaseGeometry():
    """
    class List that inherits from list
    """
    def area(self):
        """
        Raise Exception
        """
        if not isinstance(self, float):
            raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Check if the value is an instance of int
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
