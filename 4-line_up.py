#!/usr/bin/env python3
import numpy as np

def add_arrays(arr1, arr2):
    """ adds two arrays element-wise """
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    try:
        c = arr1 + arr2
        return c.tolist()
    except:
        return None