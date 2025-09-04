import unittest
from mymathlib.core import MathOperations, Calculator

class TestCoreFunctions(unittest.TestCase):
    
    def setUp(self):
        self.ops = MathOperations(precision=4)
        self.calc = Calculator()
    
    def test_addition(self):
        self.assertEqual(self.ops.add(1, 2), 3)
        self.assertEqual(self.ops.add(1.5, 2.5), 4.0)
        self.assertEqual(self.ops.add(1, 2, 3, 4), 10)
    
    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.ops.divide(10, 0)
    
    def test_calculator_chain(self):
        result = self.calc.add(5).multiply(3).subtract(2).divide(4).get_result()
        self.assertEqual(result, 3.25)
    
    def test_calculator_history(self):
        self.calc.add(10).multiply(2)
        self.assertEqual(len(self.calc.get_history()), 2)
        self.calc.clear()
        self.assertEqual(len(self.calc.get_history()), 0)

if __name__ == '__main__':
    unittest.main()