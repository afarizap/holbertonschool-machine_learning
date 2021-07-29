#!/usr/bin/env python3
""" binomial task """


class Binomial():
    """represents a binomial distribution"""

    def __init__(self, data=None, n=1, p=0.5):
        """ Initialize Binomial
            Args:
            data: list of the data used to estimate the distribution
            n: number of Bernoulli trials
            p: probability of a “success”
        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or 1 <= p:
                raise ValueError("p must be greater than 0 and less than 1")
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            variance = 0
            mean = sum(data) / len(data)
            for i in data:
                variance += (i-mean) ** 2
            variance /= len(data)
            q = variance / mean
            p = 1 - q
            n = round(mean / p)
            p = mean / n
        self.n = int(n)
        self.p = float(p)

    def pmf(self, k):
        """ Calculates the value of the PMF (probability mass function)
            for a given number of “successes”
            Args:
            k: number of “successes”
            Return: PMF value for k
        """
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0

        f_n = 1
        for i in range(1, self.n + 1):
            f_n *= i

        f_k = 1
        for i in range(1, k + 1):
            f_k *= i

        f_nk = 1
        for i in range(1, self.n - k + 1):
            f_nk *= i

        binomial_c = f_n / (f_k * f_nk)

        PMF = binomial_c * (self.p ** k) * ((1 - self.p) ** (self.n - k))
        return PMF

    def cdf(self, k):
        """ Calculates the value of the CDF (Cumulative distribution function)
            for a given number of “successes”
            Args:
            k: number of “successes”
            return: CDF value for k
        """
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        CDF = 0
        for i in range(k + 1):
            CDF += self.pmf(i)
        return CDF
