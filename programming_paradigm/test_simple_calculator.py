import unittest
from simple_calculator import SimpleCalculator
import pytest

class  TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5,2),3)
        self.assertEqual(self.calc.subtract(2, 5), -3)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3,3),9)
        self.assertEqual(self.calc.multiply(3, 10), 30)
    def test_division(self):
        self.assertEqual(self.calc.divide(6,2),3)
        self.assertEqual(self.calc.divide(3, 6), 0.5)

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            divide(5, 0)
