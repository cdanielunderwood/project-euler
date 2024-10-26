import unittest
from primes import Prime

class TestSumSquaresDifference(unittest.TestCase):

    def setUp(self):
        self.p = Prime()

    def test_get_primes(self):
        self.assertEqual([2,3,5,7,11,13], self.p.get_primes(13))

    def test_get_6th_prime(self):
        self.assertEqual(13, self.p.get_nth_prime(6))

    def test_get_100th_prime(self):
        self.assertEqual(541, self.p.get_nth_prime(100))

    def test_get_10001th_prime(self):
        self.assertEqual(104743, self.p.get_nth_prime(10001))
    

if __name__ == '__main__':
    unittest.main()