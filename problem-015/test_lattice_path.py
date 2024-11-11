import unittest
from lattice_path import LatticePath

class TestLatticePath(unittest.TestCase):

    def setUp(self):
        self.lp = LatticePath()

    def test_find_paths_2x2(self):
        self.assertEqual(6, self.lp.find_paths(2))
    
    def test_find_paths_3x3(self):
        self.assertEqual(20, self.lp.find_paths(3))

    def test_find_paths_20x20(self):
        self.assertEqual(137846528820, self.lp.find_paths(20))

if __name__ == '__main__':
    unittest.main()