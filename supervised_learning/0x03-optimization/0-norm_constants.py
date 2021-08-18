#!/usr/bin/env python3
""" 0-norm_constants task """
import numpy as np


def normalization_constants(X):
    """calculates the normalization (standardization) constants of a matrix
        X is the numpy.ndarray of shape (m, nx) to normalize
            m is the number of data points
            nx is the number of features
        Returns: the mean and standard deviation of each feature, respectively
    """
    mean = []
    stdev = []
    for i in X.T:
        mean += [i.mean()]
        stdev += [np.std(i)]
    return mean, stdev
