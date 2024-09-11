#!/usr/bin/python3
""" divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ All elements of the matrix should be divided by div """

    if type(matrix) not in [list]:
        raise TypeError("matrix must be a matrix (list of lists \
                        of integers/floats")

    for row in matrix:
        if type(row) not in [list]:
            raise TypeError("matrix must be a matrix (list of lists) \
                            of integers/floats")

    for row in matrix:
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) \
                                of integers/floats")

    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [
        [round(element / div, 2) for element in row]
        for row in matrix
    ]
    return new_matrix
