#!/usr/bin/env python3
""" normal task """


class Normal():
    """represents a normal distribution"""

    def __init__(self, data=None, mean=0., stddev=1.):
        """ class constructor

            Optional keyword arguments:
            data: list of the data used
            mean: mean of the distribution
            stddev: standard deviation of the distribution
        """
        if stddev <= 0:
            raise ValueError("stddev must be a positive value")
        if data is not None:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            a = 0
            for i in data:
                a += (i - mean) ** 2
            stddev = (a / len(data)) ** 0.5
        self.data = data
        self.mean = float(mean)
        self.stddev = float(stddev)

    def z_score(self, x):
        """ Calculates the z-score of a given x-value
            Args:
            x: is the x-value
            Returns: the z-score of x
        """
        z = (x - self.mean) / self.stddev
        return z

    def x_value(self, z):
        """ Calculates the x-value of a given z-score
            Args:
            z: is the z-score
            Returns: the x-value of z
        """
        x = (z * self.stddev) + self.mean
        return x

    def pdf(self, x):
        """ Calculates the value PDF (probability distribution function)
            for a given x-value
            Args:
            x: the x-value
            Returns: PDF value for x
        """
        e = 2.7182818285
        pi = 3.1415926536
        a = e ** (((x-self.mean)/self.stddev) ** 2 / -2)
        b = self.stddev * ((2 * pi)**0.5)
        PDF = a/b
        return PDF
