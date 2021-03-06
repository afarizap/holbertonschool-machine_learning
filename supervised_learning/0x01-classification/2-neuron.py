#!/usr/bin/env python3
""" 2-neuron task """
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
        """W get ter"""
        return self.__W

    @property
    def b(self):
        """b getter"""
        return self.__b

    @property
    def A(self):
        """A getter"""
        return self.__A

    def forward_prop(self, x):
        """ Calculates the forward propagation of the neuron
            args:
            X is a numpy.ndarray with shape (nx, m) that contains input data
            nx is the number of input features to the neuron
            m is the number of examples
        """
        z = np.matmul(self.W, x) + self.b
        self.__A = 1/(1 + np.exp(-z))
        return self.__A
