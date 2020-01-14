import unittest
import fractions as frac

class test(unittest.TestCase):
    """Simple Test"""

    def test_add(self):
        result = frac1 + frac2
        expected = frac.fraction(5, 6)
        self.assertEqual(expected.num, result.num)
        self.assertEqual(expected.den, result.den)

    
    def test_sub(self):
        result = frac1 - frac2
        expected = frac.fraction(1, 6)
        self.assertEqual(expected.num, result.num)
        self.assertEqual(expected.den, result.den)


    def test_mul(self):
        result = frac1 * frac2
        expected = frac.fraction(1, 6)
        self.assertEqual(expected.num, result.num)
        self.assertEqual(expected.den, result.den)


    def test_div(self):
        result = frac1 / frac2
        expected = frac.fraction(3, 2)
        self.assertEqual(expected.num, result.num)
        self.assertEqual(expected.den, result.den)


    def test_reduce(self):
        result = frac3.reduce()
        expected = frac.fraction(2, 5)
        self.assertEqual(expected.num, result.num)
        self.assertEqual(expected.den, result.den)


if __name__ == '__main__':
    frac1 = frac.fraction(1, 2)
    frac2 = frac.fraction(1, 3)
    frac3 = frac.fraction(12, 30)
    unittest.main()