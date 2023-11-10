#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m = []
    for i in range(len(matrix[0])):
        new = []
        for row_list in matrix:
            new.append(row_list[i] ** 2)
        m.append(new)
    return m
