#!/usr/bin/env python3
"""Gettin' Cozy"""


def cat_matrices2D(mat1, mat2, axis=0):
    """ concatenates two matrices along a specific axis """
    try:
        new = []
        for i in mat1:
            new += [i.copy()]
        if axis == 0:
            for i in mat2:
                new += [i]
            return new
        if axis == 1:
            for idx, i in enumerate(mat2):
                for j in i:
                    new[idx] += [j]
            return new
    except (ValueError, IndexError):
        return None
