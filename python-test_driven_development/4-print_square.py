#!/usr/bin/python3

def print_square(size):
    if type(size) is not [int] is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for index in range(size):
        print("#" * size)
