#!/usr/bin/env python3
import numpy as np


def cat_matrices2D(mat1, mat2, axis=0):
    """ concatenates two matrices along a specific axis """
    try:
        return np.concatenate((mat1, mat2), axis).tolist()
    except ValueError:
        return None
