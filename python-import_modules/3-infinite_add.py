#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argc, argv = len(sys.argv[1:]), sys.argv[1:]
    result = 0

    for index in range(argc):
        result += int(argv[index])
    print("{}".format(result))
