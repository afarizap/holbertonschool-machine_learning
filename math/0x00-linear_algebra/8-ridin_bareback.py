#!/usr/bin/env python3
"""Ridin’ Bareback """


def mat_mul(mat1, mat2):
    """ performs matrix multiplication """
    new = []
    y1 = len(mat1)
    x1 = len(mat1[0])
    y2 = len(mat2)
    x2 = len(mat2[0])
    if x1 != y2:
        return None
    # iterate through row of mat1
    for i in range(y1):
        y = []
        # iterate through column of mat2
        for j in range(x2):
            x = []
            # iterate through row of mat2
            for k in range(y2):
                # multiply matrix section
                x += [mat1[i][k] * mat2[k][j]]
            # sum all the products and add to matrix
            y += [sum(x)]
        # add new row to new matrix
        new += [y]
    return new
