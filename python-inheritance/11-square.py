#!/usr/bin/python3
"""
This module defines a Square class that inherits from BaseGeometry.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class used to represent a Square, inheriting from BaseGeometry.
    """
    def __init__(self, size):
        """
        Initialize the square with a size.
        Validate that size is a positive integer.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """return area of the square"""
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the
        Square object in the format [Square] size/size
        """
        return f"[Square] {self.__size}/{self.__size}"
