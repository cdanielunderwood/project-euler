import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def test_Solution(self):
        self.solution = Solution()
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
