#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None

    for submatrix in matrix:
        for i in range(len(submatrix)):