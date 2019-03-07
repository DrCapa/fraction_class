""" A simple test for fractions class """


import fractions as frac

frac1 = frac.fraction(1, 2)
frac2 = frac.fraction(1, 3)

frac3 = frac1 + frac2
assert(frac3.num == 5 and frac3.den == 6)
frac4 = frac1 - frac2
assert(frac4.num == 1 and frac4.den == 6)
frac5 = frac1 * frac2
assert(frac5.num == 1 and frac5.den == 6)
frac6 = frac1 / frac2
assert(frac6.num == 3 and frac6.den == 2)
