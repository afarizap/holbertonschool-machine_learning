#!/usr/bin/env python3
"""Slice Like A Ninja """


def np_slice(matrix, axes={}):
    """ slices a matrix along specific axes """
    new = [None] * matrix.ndim
    for k, v in axes.items():
        new[k] = slice(*v)
    new = tuple(new).copy()
    return matrix[new]