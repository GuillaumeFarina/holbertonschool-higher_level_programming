#!/usr/bin/python3
"""
function that prints a square with the character #.
"""


def print_square(size):
    """
    Check if the variable 'size' is neither an integer nor a float
    and if it is less than 0

    Check if 'size' is less than 0

    Loop to print a line of '#' of length 'size', 'size' times
    """

    if type(size) is not [int] is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for index in range(size):
        print("#" * size)
