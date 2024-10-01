#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for index in range(1, n):
        row = [1]
        for index2 in range(1, index):
            row.append(triangle[index-1][index2-1] + triangle[index-1][index2])
        row.append(1)
        triangle.append(row)
    return triangle
