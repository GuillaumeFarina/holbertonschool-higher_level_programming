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

    @property
    def position(self):
        """ retrive it """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __init__(self, size=0, position=(0, 0)):
        """
        Public instance attribute of parameter value "size=0".
        Position parameter add for position of the square
        """
        self.size = size
        self.position = position

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
            for index in range(self.position[1]):
                print("")
            for index in range(self.size):
                line = " " * self.position[0]
                line += "#" * self.size
                print(line)
