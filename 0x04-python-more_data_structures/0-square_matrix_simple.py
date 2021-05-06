#!/usr/bin/python3
def square(x):
    return x * x


def square_matrix_simple(matrix=[]):
    """function to find the square of a matrx

    Arguments:
        matrix: the given matrix

    Returns:
        a new matrix with all elements squared
    """
    new_matrix = matrix[:]
    for i in range(len(new_matrix)):
        new_matrix[i] = list(map(square, new_matrix[i]))
    return new_matrix
