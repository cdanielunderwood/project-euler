import unittest
from collatz import Collatz

class TestLongestCollatzSequence(unittest.TestCase):

    def setUp(self):
        self.col = Collatz()

    def test_collatz_sequence_start_13(self):
        self.assertEqual([13,40,20,10,5,16,8,4,2,1], self.col.get_sequence(13))
    
    def test_collatz_sequence_length_start_13(self):
        self.assertEqual(10, len(self.col.get_sequence(13)))

    def test_collatz_max_sequence_length_under_13(self):
        self.assertEqual(9, self.col.get_max_sequence_length(13))
    
    def test_collatz_max_sequence_length_under_1000000(self):
        self.assertEqual(837799, self.col.get_max_sequence_length(1000000))

if __name__ == '__main__':
    unittest.main()