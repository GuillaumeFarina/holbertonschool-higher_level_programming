#!/usr/bin/python3
"""
This is a module for Square class.
"""


class Square:
    """
    This is a class named Square.
    """
    def __init__(self, size=0):
        """
        Private instance attribute of parameter value "size=0".
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Calculate and return the area of the square.
        """
        return self.__size * self.__size
