#!/usr/bin/env python3
import numpy as np


def mat_mul(mat1, mat2):
    """ performs matrix multiplication """
    try:
        return np.matmul(mat1, mat2).tolist()
    except ValueError:
        return None
