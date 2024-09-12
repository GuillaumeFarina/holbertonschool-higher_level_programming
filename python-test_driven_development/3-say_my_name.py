#!/usr/bin/python3
"""
Function who print the name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints name "My name is <first_name> <last_name>".

    Args:
        first_name: str about the first_name.
        last_name: str about the last_name.

    Raises:
        TypeError: If first_name or last_name is not a str.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
