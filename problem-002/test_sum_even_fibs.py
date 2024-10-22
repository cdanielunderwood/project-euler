import unittest
from fibs import Fibs

class TestSumEvenFibs(unittest.TestCase):

    def setUp(self):
        self.fibs = Fibs()
    
    def test_isEvenWith2(self):
        self.assertEqual(True, self.fibs.isEven(2))
    
    def test_isEvenWith3(self):
        self.assertEqual(False, self.fibs.isEven(3))

    def test_getFibsUpTo10(self):
        self.assertEqual([1,2,3,5,8,13,21,34,55,89], self.fibs.getFibsUpTo(100))

    def test_sumEvenFibsUpTo10(self):
        self.assertEqual(44, self.fibs.sumEvenFibsUpTo(44))

    def test_sumEvenFibsUpTo4MM(self):
        self.assertEqual(4613732, self.fibs.sumEvenFibsUpTo(4000000))
    
if __name__ == '__main__':
    unittest.main()