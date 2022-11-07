from functions import skalarny
import numpy as np
import unittest

class Skalarny(unittest.TestCase):
    def test_length_scalar(self):
        s1 = [1, 2, 12, 4]
        s2 = [2, 4, 2, 8]
        s1_len = len(s1)
        s2_len = len(s2)
        #print("Zgodne rozmiary")
        self.assertEqual(s1_len, s2_len)
    def test_multiply_scalar(self):
        s1 = [1, 2, 12, 4]
        s2 = [2, 4, 2, 8]
        #print(skalarny.iloczyn(s1, s2))
        self.assertEqual(skalarny.iloczyn(s1, s2), np.sum(np.multiply(s1,s2)))

if __name__ == '__main__':
    unittest.main()
