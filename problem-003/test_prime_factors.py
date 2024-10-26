import unittest
from prime import Prime

class TestPrimeFactors(unittest.TestCase):

    def setUp(self):
       self.prime = Prime()

    def test_get_max_prime_factor_with_2(self):
        self.assertEqual(2, self.prime.get_max_prime_factor(2))
    
    def test_get_max_prime_factor_with_10(self):
        self.assertEqual(5, self.prime.get_max_prime_factor(10))

    def test_get_max_prime_factor_with_1005(self):
        self.assertEqual(67, self.prime.get_max_prime_factor(1005))

    def test_get_max_prime_factor_with_51475143(self):
        self.assertEqual(12497, self.prime.get_max_prime_factor(51475143))

    def test_get_max_prime_factor_with_600851475143(self):
        self.assertEqual(6857, self.prime.get_max_prime_factor(600851475143))
    

if __name__ == '__main__':
    unittest.main()