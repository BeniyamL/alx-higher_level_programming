#!/usr/bin/python3
""" matrix_multiplication function definition.
"""


def matrix_mul(m_a, m_b):
    """ function to multipley two matrixr

    Arguments:
        m_a: the first matrix
        m_b: the second matrix
    Returns:
        a new matrix which is a product of the two matrix
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all((isinstance(num, int) or isinstance(num, float))
               for num in [ele for row in m_a for ele in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(num, int) or isinstance(num, float))
               for num in [ele for row in m_b for ele in row]):
        raise TypeError("m_b should contain only integers or floats")
    checkRowSize(m_a, "m_a")
    checkRowSize(m_a, "m_a")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        res_row = []
        for j in range(len(m_b[0])):
            prod = 0
            for k in range(len(m_b)):
                prod += m_a[i][k] * m_b[k][j]
            res_row.append(prod)
        result.append(res_row)

    return result


def checkRowSize(matrix, which):
    """ function to check the row size of the matrix

    Arguments:
        matrix: the given matrix
        which: to indicate which matrix we are considering
    Returns:
        raise a type Error is the size is not equal
    """
    size = len(matrix[0])
    for row in matrix:
        if size != len(row):
            raise TypeError("Each row of " + which +
                            " must be of the same size")
