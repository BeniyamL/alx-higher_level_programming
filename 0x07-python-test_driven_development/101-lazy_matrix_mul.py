#!/usr/bin/python3
import numpy as np
""" lazy_matrix_mul function """


def lazy_matrix_mul(m_a, m_b):
    """ function to find the multiplication of two matrix

    Arguments:
        m_a: the first matrix
        m_b: the second matrix
    Returns:
        the product of the two matrix
    """
    return (np.matmul(m_a, m_b))
