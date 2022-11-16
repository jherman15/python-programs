import math
from math import sqrt

class ComplexNumber(object):

    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag
        print(self.real + self.imag)

    def __add__(self, other):
        print('\nSum:')
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        print('\nDifference:')
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        print('\nProduct:')
        return ComplexNumber((self.real * other.real) - (self.imag * other.imag),
                       (self.imag * other.real) + (self.real * other.imag))

    def __truediv__(self, other):
        print('\nQuotient:')
        r = (other.real ** 2 + other.imag ** 2)
        return ComplexNumber((self.real * other.real - self.imag * other.imag) / r,
                       (self.imag * other.real + self.real * other.imag) / r)