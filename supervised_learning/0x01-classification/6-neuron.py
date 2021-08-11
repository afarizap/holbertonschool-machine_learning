#!/usr/bin/env python3
""" 6-neuron task """
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
        return self.A

    def cost(self, Y, A):
        """Calculates the cost of the model using logistic regression
        args:
        Y: is a numpy.ndarray with shape (1, m) that contains
            the correct labels for the input data
        A: is a numpy.ndarray with shape (1, m) containing the
            activated output of the neuron for each example
        returns the cost
        """
        part_A = Y * np.log(A)
        part_B = (1 - Y) * np.log(1.0000001 - A)
        return float((-1 / Y.shape[1]) * np.sum(part_A + part_B))

    def evaluate(self, X, Y):
        """ Evaluates the neuron’s predictions
            args:
            X: is a numpy.ndarray with shape (nx, m) that contains the input

                nx: is the number of input features to the neuron
                m: is the number of examples

            Y: is a numpy.ndarray with shape (1, m) that contains the correct
            labels for the input data
            Returns: the neuron’s prediction and the cost of the network,
             respectively
            The prediction should be a numpy.ndarray with shape (1, m)
             containing the predicted labels for each example
            The label values should be 1 if the output of the network
             is >= 0.5 and 0 otherwise
        """
        A = self.forward_prop(X)
        cost = self.cost(Y, A)
        prediction = np.zeros((1, Y.shape[1]), dtype=int)
        prediction[A >= 0.5] = 1
        return prediction, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """
        Add the public method def gradient_descent(self, X, Y, A, alpha=0.05):
        Calculates one pass of gradient descent on the neuron
        X is a numpy.ndarray with shape (nx, m) that contains the input data
            nx is the number of input features to the neuron
            m is the number of examples
        Y is a numpy.ndarray with shape (1, m) that contains the correct
         labels for the input data
        A is a numpy.ndarray with shape (1, m) containing the activated output
         of the neuron for each example
        alpha is the learning rate
        Updates the private attributes __W and __b
        """
        m = Y.shape[1]
        dZ = A - Y
        dW = np.matmul(dZ, X.T) / m
        db = np.sum(dZ) / m
        self.__W = self.W - alpha * dW
        self.__b = self.b - alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """
    Trains the neuron
    X is a numpy.ndarray with shape (nx, m) that contains the input data
        nx is the number of input features to the neuron
        m is the number of examples
    Y is a numpy.ndarray with shape (1, m) that contains the correct labels
     for the input data
    iterations is the number of iterations to train over
    alpha is the learning rate
    Returns the evaluation of the training data after iterations of training
     have occurred
        """
        if type(iterations) is not int:
            raise TypeError("iterations must be an integer")
        if iterations < 1:
            raise ValueError("iterations must be a positive integer")
        if type(alpha) is not float:
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")

        A = self.forward_prop(X)
        for i in range(iterations):
            self.gradient_descent(X, Y, A, alpha)
            A = self.forward_prop(X)
        return self.evaluate(X, Y)
