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

    def cdf(self, x):
        """ Calculates the value of the CDF (cumulative distribution function)
            for a given x-value
            Args:
            x: the x-value
            Returns: CDF value for x
            https://www.itl.nist.gov/div898/handbook/eda/section3/eda3661.htm
        """
        pi = 3.1415926536

        y = (x - self.mean) / (self.stddev * (2 ** 0.5))
        erf1 = y
        erf2 = (y ** 3) / 3
        erf3 = (y ** 5) / 10
        erf4 = (y ** 7) / 42
        erf5 = (y ** 9) / 216
        erf6 = 2 / (pi ** 0.5)
        erf = erf6 * (erf1 - erf2 + erf3 - erf4 + erf5)

        CDF = (1 + erf) / 2
        return CDF
