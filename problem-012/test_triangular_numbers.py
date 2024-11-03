import unittest
from triangular_numbers import TriangularNumber

class TestTriangularNumbers(unittest.TestCase):

    def setUp(self):
        self.tn = TriangularNumber()

    def test_sum_triangular_number(self):
        self.assertEqual(28, self.tn.sum_triangular_number(7))

    def test_get_primes(self):
        self.assertEqual([2,3,5,7,11,13], self.tn.get_primes(13))

    def test_get_divisors_with_2(self):
        self.assertEqual([1,2], self.tn.get_divisors(2)) 
    
    def test_get_divisors_with_24(self):
        self.assertEqual([1,2,3,4,6,8,12,24], self.tn.get_divisors(24)) 

    def test_get_divisors_with_96(self):
        self.assertEqual([1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 96], self.tn.get_divisors(96)) 

    def test_get_divisors_with_60(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60], self.tn.get_divisors(60)) 

    def test_find_first_triangular_number_with_6_divisors(self):
        print("test_find_first_triangular_number_with_6_divisors")
        result = self.tn.find_first_triangular_number_by_number_of_divisors(6)
        print(repr(result))
        self.assertTrue(28==result[1], 6==result[3])

    def test_find_first_triangular_number_with_101_divisors(self):
        print("test_find_first_triangular_number_with_101_divisors")
        result = self.tn.find_first_triangular_number_by_number_of_divisors(101)
        print(repr(result))
        self.assertTrue(73920==result[1], 101==result[3])
    
    def test_find_first_triangular_number_with_501_divisors(self):
        print("test_find_first_triangular_number_with_501_divisors")
        result = self.tn.find_first_triangular_number_by_number_of_divisors(501)
        print(f'result[0]={result[0]}, result[1]={result[1]}, result[3]={result[3]}')
        self.assertTrue(76576500==result[1], 576==result[3])


if __name__ == '__main__':
    unittest.main()