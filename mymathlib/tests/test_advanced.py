import unittest
from mymathlib.advanced import AdvancedMath, Statistics

class TestAdvancedFunctions(unittest.TestCase):
    
    def test_factorial(self):
        self.assertEqual(AdvancedMath.factorial(0), 1)
        self.assertEqual(AdvancedMath.factorial(1), 1)
        self.assertEqual(AdvancedMath.factorial(5), 120)
        self.assertEqual(AdvancedMath.factorial(10), 3628800)
        
        with self.assertRaises(ValueError):
            AdvancedMath.factorial(-1)
    
    def test_is_prime(self):
        self.assertTrue(AdvancedMath.is_prime(2))
        self.assertTrue(AdvancedMath.is_prime(3))
        self.assertTrue(AdvancedMath.is_prime(17))
        self.assertFalse(AdvancedMath.is_prime(1))
        self.assertFalse(AdvancedMath.is_prime(4))
        self.assertFalse(AdvancedMath.is_prime(10))
    
    def test_fibonacci(self):
        self.assertEqual(AdvancedMath.fibonacci(0), [])
        self.assertEqual(AdvancedMath.fibonacci(1), [0])
        self.assertEqual(AdvancedMath.fibonacci(2), [0, 1])
        self.assertEqual(AdvancedMath.fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(AdvancedMath.fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    
    def test_power(self):
        self.assertEqual(AdvancedMath.power(2, 3), 8)
        self.assertEqual(AdvancedMath.power(5, 0), 1)
        self.assertEqual(AdvancedMath.power(10, -1), 0.1)
    
    def test_sqrt(self):
        self.assertEqual(AdvancedMath.sqrt(4), 2.0)
        self.assertAlmostEqual(AdvancedMath.sqrt(2), 1.4142, places=4)
        
        with self.assertRaises(ValueError):
            AdvancedMath.sqrt(-1)

class TestStatistics(unittest.TestCase):
    
    def test_mean(self):
        self.assertEqual(Statistics.mean([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(Statistics.mean([10, 20, 30]), 20.0)
        
        with self.assertRaises(ValueError):
            Statistics.mean([])
    
    def test_median(self):
        self.assertEqual(Statistics.median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(Statistics.median([1, 2, 3, 4, 5, 6]), 3.5)
        
        with self.assertRaises(ValueError):
            Statistics.median([])
    
    def test_mode(self):
        self.assertEqual(Statistics.mode([1, 2, 2, 3, 4]), [2])
        self.assertEqual(Statistics.mode([1, 2, 2, 3, 3, 4]), [2, 3])
        
        with self.assertRaises(ValueError):
            Statistics.mode([])

if __name__ == '__main__':
    unittest.main()