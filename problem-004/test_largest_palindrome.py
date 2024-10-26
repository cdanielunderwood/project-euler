import unittest
from palindrome import Palindrome

class TestLargestPalindromeProduct(unittest.TestCase):

    def setUp(self):
        self.p = Palindrome()

    def test_is_palindrome(self):
        self.assertEqual([True, False, True, True], [self.p.is_palindrome(n) for n in [2, 20, 202, "tacocat"]])

    def test_max_palindrome_product_with_1(self):
        self.assertEqual(9, self.p.max_palidrome_product(1))
    
    def test_max_palindrome_product_with_2(self):
        self.assertEqual(9009, self.p.max_palidrome_product(2))
    
    def test_max_palindrome_product_with_3(self):
        self.assertEqual(906609, self.p.max_palidrome_product(3))


if __name__ == '__main__':
    unittest.main()