import unittest
from largest_product import LargestProduct

class TestLargestProduct(unittest.TestCase):

    def setUp(self):
        self.lp = LargestProduct()
        self.lp.append_series("73167176531330624919225119674426574742355349194934")
        self.lp.append_series("96983520312774506326239578318016984801869478851843")
        self.lp.append_series("85861560789112949495459501737958331952853208805511")
        self.lp.append_series("12540698747158523863050715693290963295227443043557")
        self.lp.append_series("66896648950445244523161731856403098711121722383113")
        self.lp.append_series("62229893423380308135336276614282806444486645238749")
        self.lp.append_series("30358907296290491560440772390713810515859307960866")
        self.lp.append_series("70172427121883998797908792274921901699720888093776")
        self.lp.append_series("65727333001053367881220235421809751254540594752243")
        self.lp.append_series("52584907711670556013604839586446706324415722155397")
        self.lp.append_series("53697817977846174064955149290862569321978468622482")
        self.lp.append_series("83972241375657056057490261407972968652414535100474")
        self.lp.append_series("82166370484403199890008895243450658541227588666881")
        self.lp.append_series("16427171479924442928230863465674813919123162824586")
        self.lp.append_series("17866458359124566529476545682848912883142607690042")
        self.lp.append_series("24219022671055626321111109370544217506941658960408")
        self.lp.append_series("07198403850962455444362981230987879927244284909188")
        self.lp.append_series("84580156166097919133875499200524063689912560717606")
        self.lp.append_series("05886116467109405077541002256983155200055935729725")
        self.lp.append_series("71636269561882670428252483600823257530420752963450")    
    
    def test_set_series(self):
        self.assertEqual(1000, len(self.lp.get_series()))

    def test_get_slices_with_4(self):
        slices = self.lp.get_slices(4)
        self.assertEqual(len(self.lp.get_series())-4, len(slices))

    def test_find_largest_product_with4(self):
       self.assertEqual(5832, self.lp.find_largest_product(4))

    def test_find_largest_product_with13(self):
       self.assertEqual(23514624000, self.lp.find_largest_product(13))

    

if __name__ == '__main__':
    unittest.main()