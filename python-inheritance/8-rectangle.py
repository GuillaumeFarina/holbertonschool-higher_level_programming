#!/usr/bin/python3
"""This is a docstring for the module."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initialize width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
