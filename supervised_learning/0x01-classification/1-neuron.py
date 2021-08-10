#!/usr/bin/env python3
""" 1-neuron task """
import numpy as np


class Neuron:
    """Defines a single neuron performing a binary
    classification"""

    def __init__(self, nx):
        """class constructor
            args:
            nx: number of input features to the neuron
            public instance attributes:
            w: weights vector for the neuron(random normal dist)
            b: bias for the neuron(0)
            A: activated output of the neuron(prediction)(0)
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """W getter"""
        return self.__W

    @property
    def b(self):
        """b getter"""
        return self.__b

    @property
    def A(self):
        """A getter"""
        return self.__A
