#!/usr/bin/env python3
import numpy as np
""" 0-neuron task """


class Neuron:
    """Defines a single neuron performing a binary
    classification"""

    def __init__(self, nx):
        """class constructor
            args:
            nx: number of input features to the neuron
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        """public instance attributes:
            w: weights vector for the neuron(random normal dist)
            b: bias for the neuron(0)
            A: activated output of the neuron(prediction)(0)
        """
        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0
