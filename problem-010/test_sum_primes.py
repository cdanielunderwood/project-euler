import unittest
from primes import Prime

class TestSumPrimes(unittest.TestCase):

    def setUp(self):
        self.p = Prime()

    def test_get_primes(self):
        self.assertEqual([2,3,5,7,11,13], self.p.get_primes(13))

    def test_get_6th_prime(self):
        self.assertEqual(13, self.p.get_nth_prime(6))

    def test_get_100th_prime(self):
        self.assertEqual(541, self.p.get_nth_prime(100))

    def test_sum_primes_below_10(self):
        self.assertEqual(17,self.p.sum_primes(10))

    def test_sum_primes_below_2000000(self):
        self.assertEqual(142913828922,self.p.sum_primes(2000000))

if __name__ == '__main__':
    unittest.main()