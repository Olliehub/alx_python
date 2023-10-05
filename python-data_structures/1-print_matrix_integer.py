#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None

    for submatrix in matrix:
        for i in range(len(submatrix)):
            print("{:d}".format(submatrix[i]), end="")
            if i < len(submatrix) - 1:
                print(" ", end="")
        print()

matrix = [[1,2,3], [4,5,6], [7,8,9]]
print_matrix_integer(matrix)
