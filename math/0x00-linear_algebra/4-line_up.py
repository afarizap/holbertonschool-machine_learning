#!/usr/bin/env python3
""" Line up """


def add_arrays(arr1, arr2):
    """ adds two arrays element-wise returns a new list """
    try:
        return [arr1[i] + arr2[i]for i in range(len(arr1))]
    except (IndexError, ValueError):
        return None
