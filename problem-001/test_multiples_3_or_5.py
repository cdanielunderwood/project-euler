import unittest
from multiples import Multiples

class TestMultiples3or5(unittest.TestCase):
    
    def test_MultiplesOf3_with3(self):
        self.multiples = Multiples()
        self.assertEqual(True, self.multiples.isMultipleOf3(3))

    def test_MultiplesOf3_with4(self):
        self.multiples = Multiples()
        self.assertEqual(False, self.multiples.isMultipleOf3(4))

    def test_MultiplesOf3_with81(self):
        self.multiples = Multiples()
        self.assertEqual(True, self.multiples.isMultipleOf3(81))

    def test_MultiplesOf5_with5(self):
        self.multiples = Multiples()
        self.assertEqual(True, self.multiples.isMultipleOf5(5))

    def test_MultiplesOf5_with6(self):
        self.multiples = Multiples()
        self.assertEqual(False, self.multiples.isMultipleOf5(6))

    def test_SumMultiplesOf3And5Below10(self):
        self.multiples = Multiples()
        self.assertEqual(23, self.multiples.sumMultiplesOf3And5(10))

    def test_SumMultiplesOf3And5Below1000(self):
        self.multiples = Multiples()
        self.assertEqual(233168, self.multiples.sumMultiplesOf3And5(1000))



if __name__ == '__main__':
    unittest.main()

