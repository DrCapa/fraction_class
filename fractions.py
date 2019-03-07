""" A simple class for some operations with fractions """


class fraction:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator

    def __del__(self):
        print('delete fraction')

    def show(self):
        print('%i / %i' % (self.num, self.den))

    def __add__(self, other):
        num = self.num*other.den+other.num*self.den
        den = self.den*other.den
        return fraction(num, den)

    def __sub__(self, other):
        num = self.num*other.den-other.num*self.den
        den = self.den*other.den
        return fraction(num, den)

    def __mul__(self, other):
        num = self.num*other.num
        den = self.den*other.den
        return fraction(num, den)

    def __truediv__(self, other):
        num = self.num*other.den
        den = self.den*other.num
        return fraction(num, den)
