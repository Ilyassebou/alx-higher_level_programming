#!/usr/bin/python3
"""Module for matrix_divided method"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix: The matrix whose elements are to be divided by div.
        div: The dividing number.

    Raises:
        TypeError: if matrix is not a list of lists of int or float.
        TypeError: if each row of matrix is not of the same size.
        TypeError: if div is neither an int nor float
        ZeroDivisionError: if div is zero

    Returns:
        a new matrix with elements rounded to 2 decimal places.
    """

    def validate_matrix(m):
        if not isinstance(m, list) or len(m) == 0 or not m[0]:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        for row in m:
            if len(row) == 0:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            for x in row:
                if type(x) is not int and type(x) is not float:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        len_rows = [len(row) for row in m]
        if not all(elem == len_rows[0] for elem in len_rows):
            raise TypeError("Each row of the matrix must have the same size")

    def validate_divisor(d):
        if type(d) is not int and type(d) is not float:
            raise TypeError("div must be a number")
        if d == 0:
            raise ZeroDivisionError("division by zero")

    validate_matrix(matrix)
    validate_divisor(div)

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix
