from simple_calculator import SimpleCalculator
import unittest

class Test_Simple_Claculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
    def test_add(self):
        self.assertEqual(SimpleCalculator.add(5,5), 10)
        self.assertEqual(SimpleCalculator.add(5.5,5.7), 11.2)
    def test_subtract(self):
        self.assertEqual(SimpleCalculator.subtract(5,5), 0)
        self.assertEqual(SimpleCalculator.subtract(5.5,5.7), -0.2)
    def test_multiply(self):
        self.assertEqual(SimpleCalculator.multiply(5,5), 25)
        self.assertEqual(SimpleCalculator.multiply(5.5,-1), -5.5)
    def test_divide(self):
        self.assertEqual(SimpleCalculator.divide(5,5), 1)
        self.assertEqual(SimpleCalculator.divide(5.5,11), 0.5)
        self.assertEqual(SimpleCalculator.divide(-5.5,11), -0.5)
        self.assertEqual(SimpleCalculator.divide(5.5,0), None)
