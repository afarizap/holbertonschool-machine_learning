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
