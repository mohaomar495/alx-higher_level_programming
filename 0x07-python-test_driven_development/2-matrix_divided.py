#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div=1):
    """
    Return a new matrix which is the result
    of the original matrix divided by div.

    :param matrix: matrix (list of lists) of integers/floats
    :param div: div should be integer/float and also it should not be zero.
    :return: new matrix divided by div.
    """
    if (
        not isinstance(matrix, list)
        or matrix == []
        or not all(isinstance(row, list) for row in matrix)
        or not all(
            (isinstance(elem, int) or isinstance(elem, float))
            for elem in [num for row in matrix for num in row]
        )
    ):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)
    return new_matrix
