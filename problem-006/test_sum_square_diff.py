import unittest
from sum_square import SumSquares

class TestSumSquaresDifference(unittest.TestCase):

    def setUp(self):
        self.ss = SumSquares()

    def test_sum_squares(self):
        self.assertEqual(385, self.ss.sum_squares(10))
    
    def test_square_sums(self):
        self.assertEqual(3025, self.ss.square_sums(10))

    def test_sum_square_diff(self):
        self.assertEqual(2640, self.ss.square_sum_diff(10))

    def test_sum_square_diff_answer(self):
        self.assertEqual(25164150, self.ss.square_sum_diff(100))
    

if __name__ == '__main__':
    unittest.main()