#!/usr/bin/env python3
"""Across the planes"""


def add_matrices2D(mat1, mat2):
    """  adds two matrices element-wise """
    try:
        new = []
        if len(mat1) != len(mat2):
            return ValueError
        for i in range(len(mat1)):
            if len(mat1[i]) != len(mat2[i]):
                raise ValueError
            x = []
            for n in range(len(mat1[i])):
                t = mat1[i][n] + mat2[i][n]
                x += [t]
            new += [x]
        return new
    except (ValueError, IndexError):
        return None
