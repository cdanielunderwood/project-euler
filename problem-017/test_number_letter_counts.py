import unittest
from number_letter_counts import NumberLetterCounts

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.nlc = NumberLetterCounts()
    
    def test_count_letters_in_number(self):
        self.assertEqual(3, self.nlc.count_letters_in_number(1))
        self.assertEqual(3, self.nlc.count_letters_in_number(10))
        self.assertEqual(len('seventeen'), self.nlc.count_letters_in_number(17))
        self.assertEqual(len('twenty'), self.nlc.count_letters_in_number(20))
        self.assertEqual(len('twentyone'), self.nlc.count_letters_in_number(21))
        self.assertEqual(len('ninetynine'), self.nlc.count_letters_in_number(99))
        self.assertEqual(len('onehundred'), self.nlc.count_letters_in_number(100))
        self.assertEqual(len('onehundredandone'), self.nlc.count_letters_in_number(101))
        self.assertEqual(len('ninehundredandninetynine'), self.nlc.count_letters_in_number(999))
        self.assertEqual(len('onethousand'), self.nlc.count_letters_in_number(1000))
        self.assertEqual(len('onethousandandeight'), self.nlc.count_letters_in_number(1008))

    def test_count_numbers_to_5(self):
        x = sum([self.nlc.count_letters_in_number(i) for i in range(1,6)])
        self.assertEqual(19, x)

    def test_count_numbers_to_1000(self):
        x = sum([self.nlc.count_letters_in_number(i) for i in range(1,1001)])
        self.assertEqual(21124, x)


if __name__ == '__main__':
    unittest.main()
