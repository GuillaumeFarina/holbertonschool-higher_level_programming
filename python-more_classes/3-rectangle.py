#!/usr/bin/python3
"""
This is a module for Rectangle class
"""


class Rectangle:
    """
    This is a class named Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.
        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Getter method for the width attribute.
        Returns the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.
        Ensures the width is an integer and greater than or equal to 0.
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.
        Returns the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.
        Ensures the height is an integer and greater than or equal to 0.
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        If either width or height is 0, returns 0.
        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """
        Print lines of '#' with the specified width and return the last line
        """
        if self.width == 0 or self.height == 0:
            print("")
        else:
            for index in range(self.height-1):
                print(str('#') * self.width)
        return (str('#') * self.width)
