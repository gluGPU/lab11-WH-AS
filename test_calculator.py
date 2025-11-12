# https://github.com/gluGPU/lab11-WH-AS/tree/main
# Partner 1: Will Hudspeth
# Partner 2: Amana Southichack

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(10, 12), 22)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(10, 7), 3)
        self.assertEqual(subtract(1000, 1000), 0)
    ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(10, mul(2, 5))
        self.assertAlmostEqual(0.333, mul(1, 0.333))
        self.assertEqual(1000, mul(100, 10))

    def test_divide(self):
        self.assertEqual(div(2, 10), 5)
        self.assertAlmostEqual(div(10, 5), 0.5)
        self.assertEqual(div(2, 8), 4)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 4), 2)
        self.assertEqual(logarithm(3, 27), 3)
        self.assertEqual(logarithm(2, 32), 5)

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(0, 10)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)
    
    def test_hypotenuse(self):
        self.assertAlmostEqual(10.44031, hypotenuse(3, 10), 4)
        self.assertEqual(5, hypotenuse(4, 3))
        self.assertAlmostEqual(22.36068, hypotenuse(20, 10), 4)
    
    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-1)
        
        self.assertEqual(0, square_root(0))
        self.assertEqual(10, square_root(100))

# Do not touch this
# im gonna touch it
if __name__ == "__main__":
    unittest.main()