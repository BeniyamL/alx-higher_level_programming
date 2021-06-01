#!/usr/bin/python3
""" function definiton for pascal_triangle """


def pascal_triangle(n):
    """ function to print a pascal triangle

    Arguments:
        n: the number of rows of a triangle
    Returns:
        the passcal triangle
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(n - 1):
        last_row = triangle[-1]
        row = [1]
        for j in range(len(last_row) - 1):
            row.append(last_row[j] + last_row[j + 1])
        row.append(1)
        triangle.append(row)
    return triangle
