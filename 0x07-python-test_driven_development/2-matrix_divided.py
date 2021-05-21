#!/usr/bin/python3
""" matrix division by some number.
for this function, the matrix must be a list of lists of integers or floats and
each row of the matrix must be of the same size.
the number which divides the matrix must be different from 0

"""


def matrix_divided(matrix, div):
    """ function to divid a matrix by a number

    Arguments:
        matrix: the given matrix
        div: the number which divides the matrix
    Returns:
        a new matrix which was divedied by div
    """
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    if not all((isinstance(num, int) or isinstance(num, float))
               for num in [ele for row in matrix for ele in row]):
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    checkRowSize(matrix)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])


def checkRowSize(matrix):
    """ function to check the row size of the matrix

    Arguments:
        matrix: the given matrix
    Returns:
        raise a type Error is the size is not equal
    """
    size = len(matrix[0])
    for row in matrix:
        if size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
