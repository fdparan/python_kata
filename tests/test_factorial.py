import unittest
import math
import random

#TODO: Running the command line unittest on this script
# doesn't work in 2.7. This import line could likely be
# main suspect.
from src import factorial

class TestFactorial(unittest.TestCase):

    def test_factorial(self):
        for n,f in [(1,1), (2,2), (3,6), (4, 24), (5,120)]:
            self.assertEqual(factorial.factorial(n), f)
    
    def test_factorial_on_random_number(self):
        number = random.randint(1,100)

        self.assertEqual(factorial.factorial(number), math.factorial(number))

    def test_factorial_on_zero(self):
        self.assertEqual(factorial.factorial(0), 1)

    def test_factorial_on_negative_number_raises_value_error(self):
        with self.assertRaises(ValueError):
            factorial.factorial(-1)

if __name__ == '__main__':
    unittest.main()
