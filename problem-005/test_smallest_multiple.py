import unittest
from multiples import Multiples

class TestSmallestMultiple(unittest.TestCase):

    def setUp(self):
        self.m = Multiples()

    def test_is_factor(self):
        self.assertEqual([True, False], [self.m.is_factor(2,4), self.m.is_factor(2,3)])

    def test_smallest_multiple_range_10(self):
        self.assertEqual(2520,self.m.smallest_multiple(10))

    def test_smallest_multiple_range_20(self):
        self.assertEqual(232792560,self.m.smallest_multiple(20))


if __name__ == '__main__':
    unittest.main()