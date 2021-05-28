from __future__ import division


class Rational:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numer = numerator  
        self.denom = denominator


    def __eq__(self, other):
        # If both numerator is zero, then it is equally zero
        if self.numer == 0 and other.numer == 0:
            return True

        # Reduce the numbers before comparing it
        # e.g, 25/100 is equal to 1/4
        a1, b1 = self.reduce(self.numer, self.denom)
        a2, b2 = self.reduce(other.numer, other.denom)
        return a1 == a2 and b1 == b2


    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)


    def __add__(self, other):
        # a1/b + a2/b = a1 * a2 / b
        if self.denom == other.denom:
            numer = self.numer + other.numer
            denom = self.denom
        # a1/b1 + a2/b2 = (a1 * b2 + a2 * b1) / (b1 * b2)
        else:
            numer = self.numer * other.denom + other.numer * self.denom
            denom = self.denom * other.denom

        return self.check_if_numerator_is_zero(numer, denom)


    def __sub__(self, other):
        # a1/b - a2/b = a1 * a2 / b
        if self.denom == other.denom:
            numer = self.numer - other.numer
            denom = self.denom
        # a1/b1 - a2/b2 = (a1 * b2 - a2 * b1) / (b1 * b2)
        else:
            numer = self.numer * other.denom - other.numer * self.denom
            denom = self.denom * other.denom

        return self.check_if_numerator_is_zero(numer, denom)


    def __mul__(self, other):
        # a1/b1 * a2/b2 = a1*a2/b1*b2
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return self.check_if_numerator_is_zero(numer, denom)


    def __truediv__(self, other):
        # a1/b1 : a2/b2 = a1*b2/a2*b1
        if self.denom == 0 or other.denom == 0:
            raise ValueError("Denominator of the result is zero.")

        numer = self.numer * other.denom
        denom = other.numer * self.denom

        # Instead of 3/-4, write it as -3/4
        if denom < 0:
            numer, denom = -numer, -denom
        return Rational(numer, denom)


    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))


    def __pow__(self, power):
        if power < 0:
            power = abs(power)
        return Rational(self.numer ** power, self.denom ** power)


    def __rpow__(self, base):
        return base ** (self.numer / self.denom)


    def check_if_numerator_is_zero(self, numerator, denominator):
        # Rationals with numerator of zero, like 0/99 or 0/5, is equal to 0.0
        # Therefore the rational number should be simplified into 0/1
        if numerator == 0:
            return Rational(0, 1)
        else:
            return Rational(numerator, denominator)


    def reduce(self, numerator, denominator):
        numerator, denominator = abs(numerator), abs(denominator)
        i = 2

        while i <= numerator and i <= denominator:
            while numerator % i == 0 and denominator % i == 0:
                numerator, denominator = numerator / i, denominator / i
            i += 1

        return numerator, denominator
        
