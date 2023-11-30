#!/usr/bin/python3
""" A matrix Function with Test """


def matrix_divided(matrix, div):
    """ matrix function

    round figure to be divided by idv

    """

    if not isinstance(matrix, list) or len(matrix) == 0:
        er = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError("{}".format(er))

    if not all(isinstance(row, list) or len(row) == 0 for row in matrix):
        err = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError("{}".format(err))

    if not all(isinstance(e, (int, float)) for row in matrix for e in row):
        err = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError("{}".format(err))

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if any(not row for row in matrix):
        err = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError("{}".format(err))

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round((i / div), 2) for i in row] for row in matrix]
    return result


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/2-matrix_divided.txt")
