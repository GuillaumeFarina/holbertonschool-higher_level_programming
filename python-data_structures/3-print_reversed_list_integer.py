#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    my_list_reverse = list(reversed(my_list))
    for number in my_list_reverse:
        print("{}".format(number))
