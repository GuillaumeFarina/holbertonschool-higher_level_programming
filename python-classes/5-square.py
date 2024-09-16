#!/usr/bin/python3
"""This is a module for Square class."""


class Square:
    """This is a class named Square."""

    @property
    def size(self):
        """Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def __init__(self, size=0):
        """Public instance attribute of parameter value "size=0"."""
        self.size = size

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """ Prints the square with the character #.
            If size == 0, print empty line.
        """
        if self.size == 0:
            print("")
        else:
            for _ in range(self.size):
                print("#" * self.size)
