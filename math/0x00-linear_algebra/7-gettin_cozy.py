#!/usr/bin/env python3
"""Gettin' Cozy"""


def cat_matrices2D(mat1, mat2, axis=0):
    """ concatenates two matrices along a specific axis """
    try:
        new = []
        if axis == 0:
            for i in mat1:
                new += [i.copy()]
            for i in mat2:
                new += [i.copy()]
            return new
        if axis == 1:
            for i in range(len(mat1)):
                new += [mat1[i].copy() + mat2[i].copy()]
            return new
    except (ValueError, IndexError):
        return None
