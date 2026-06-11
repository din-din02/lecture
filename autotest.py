import unittest
import math as m

def equation(a, b):
    y = m.sqrt((a + b) ** 3 / (a - b) ** 2)
    return round(y, 4)

class TestAddFunction(unittest.TestCase):
    def test_integer_positive_numbers(self):
        self.assertEqual(equation(2, 3), 11.1803)

    def test_integer_negative_numbers(self):
        self.assertEqual(equation(-1, -1), ZeroDivisionError)

    def test_zero(self):
        self.assertEqual(equation(0, 0), ZeroDivisionError)

if __name__ == "__main__":
    unittest.main()
