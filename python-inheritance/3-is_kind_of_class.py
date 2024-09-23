#!/usr/bin/python3
"""
This line specifies the interpreter to be used for executing the script
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class.

    Parameters:
    obj: The object to check.
    a_class: The class to match the type of obj against.

    Returns:
    bool: True if obj is an instance or subclass instance of a_class,
    otherwise False.
    """
    return isinstance(obj, a_class)
