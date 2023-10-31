#!/usr/bin/python3
"""
h
e
y
"""


def matrix_divided(matrix, div):
    """
    in fun
    """

    length = 0
    if len(matrix) != 0:
        length = len(matrix[0])
    if (not isinstance(matrix, list) or
            length == 0 or
            not all(isinstance(row, list) and
                 all(isinstance(num, (int, float)) for num in row)
                for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists)" +
                " of integers/floats")
    for i in matrix:
        if len(i) != length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
