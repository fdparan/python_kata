import unittest
import math
import random
from src import factorial

class TestFactorial(unittest.TestCase):

    def test_factorial(self):
        for n,f in [(1,1), (2,2), (3,6), (4, 24), (5,120)]:
            self.assertEqual(factorial.factorial(n), f)
    
    def test_factorial_on_random_number(self):
        number = random.randint(1,100)

        print('Random number: %d'%number)

        self.assertEqual(factorial.factorial(number), math.factorial(number))

if __name__ == '__main__':
    unittest.main()
