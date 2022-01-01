from distance_metric import *
import unittest

class TestEuclidean1D(unittest.TestCase):
    def test_calc_distance_1d(self):
        self.assertEqual(calc_distance(1, 10), 9)

if __name__ == '__main__':
    unittest.main()
