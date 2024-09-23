#!/usr/bin/python3
"""
This is a docstring for the module, which is currently empty
"""


class MyList(list):
    """
    class MyList that inherits from list
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))
