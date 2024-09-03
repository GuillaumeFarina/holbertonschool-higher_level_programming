#!/usr/bin/python3

for index in range(0, 9):
    for index_2 in range(index + 1, 10):
        if (index != 8 or index_2 != 9):
            print("{}{}".format(index, index_2), end=", ")
        else:
            print("{}{}".format(index, index_2))
