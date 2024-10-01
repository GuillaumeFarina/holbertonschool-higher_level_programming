#!/usr/bin/python3
""" read (r) """


def read_file(filename=""):
    """ function who read the file """
    with open(filename, encoding="utf-8") as my_file_0:
        print(my_file_0.read(), end="")
