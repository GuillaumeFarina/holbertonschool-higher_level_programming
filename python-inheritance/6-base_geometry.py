#!/usr/bin/python3
"""
This is a docstring for the module.
"""


class BaseGeometry():
    """
    class List that inherits from list
    """
    def area(self):
        if not isinstance(self, float):
            raise Exception("area() is not implemented")
