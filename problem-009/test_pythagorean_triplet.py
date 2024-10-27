import unittest
from pythagorean_triplet import PythagoreanTriplet

class TestPythagoreanTriplet(unittest.TestCase):

    def setUp(self):
        self.pt = PythagoreanTriplet()   
    
    def test_is_pythagorean_triplet_with_3_4_5(self):
        self.assertTrue(self.pt.is_pythagorean_triplet(3,4,5))
   
    def test_get_product_of_triplet_with_3_4_5(self):
        self.assertEqual(60,self.pt.get_product_of_triplet(3,4,5))

    def test_find_special_sum_triplet(self):
        self.assertEqual(31875000, self.pt.find_special_sum_triplet(1000))
    

if __name__ == '__main__':
    unittest.main()