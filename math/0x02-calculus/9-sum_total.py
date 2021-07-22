#!/usr/bin/env python3
"""defines a function to sumate a square"""


def summation_i_squared(n):
    """get the series of a squared sequence"""
    try:
        n = int(n)
        if n < 1:
            return None
    except:
        return None
    return int((n * (n+1) * (2*n + 1)) / 6)
