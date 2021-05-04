#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    print_matrix_integer - print matrix of an integer
    @matrix: the given matrix
    @Return : nothing
    """

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == len(matrix[i]) - 1:
                print("{:d}".format(matrix[i][j]), end="")
            else:
                print("{:d}".format(matrix[i][j]), end=" ")
        print()
