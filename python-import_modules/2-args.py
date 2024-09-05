#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argc, argv = len(sys.argv[1:]), sys.argv[1:]

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))

    for index in range(argc):
        print("{}: {}".format(index + 1, argv[index]))
