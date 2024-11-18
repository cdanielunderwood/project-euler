import unittest
from power_digit_sum import PowerDigitSum

class TestPowerDigitSum(unittest.TestCase):

    def setUp(self):
        self.pds = PowerDigitSum()

    def test_sum_of_digits_2_to_the_3(self):
        self.assertEqual(8, self.pds.sum_digits_base_2(3))

    def test_sum_of_digits_2_to_the_15(self):
        self.assertEqual(26, self.pds.sum_digits_base_2(15))
    
    def test_sum_of_digits_2_to_the_1000(self):
        self.assertEqual(1366, self.pds.sum_digits_base_2(1000))

if __name__ == '__main__':
    unittest.main()