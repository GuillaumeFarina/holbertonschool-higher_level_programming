#!/usr/bin/python3
"""
    function called add_integer that takes two arguments, a and b.

    checks if the type of a is not int or float. If it’s not.
"""


def add_integer(a, b=98):
    """
    converts a and b to integers (int) and returns their sum.
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
