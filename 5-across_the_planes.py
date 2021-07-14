#!/usr/bin/env python3
import numpy as np

def add_matrices2D(mat1, mat2):
    """  adds two matrices element-wise """
    mat1 = np.array(mat1)
    mat2 = np.array(mat2)
    try:
        c = mat1 + mat2
        return c.tolist()
    except:
        return None
