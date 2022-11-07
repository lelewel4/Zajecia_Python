from functions import rownanie_kwadratowe
import numpy as np
import unittest

class Kwadratowa(unittest.TestCase):
    def test_delta_positive(self):
        a = 1;
        b = -4;
        c = -36;
        d = rownanie_kwadratowe.kwadratowe(a, b, c)
        d = np.array(d)
        e = np.roots([a, b, c])
        self.assertEqual(d.any(), e.any())
    def test_delta_zero(self):
        a = 1;
        b = 2;
        c = 1;
        d = rownanie_kwadratowe.kwadratowe(a, b, c)
        d = np.array(d)
        e = np.roots([a, b, c])
        self.assertEqual(d.any(), e.any())
    def test_delta_negative(self):                      #test czy aby nasza funkcja nie liczy MZ dla ujemnej delty
        a = 1;
        b = 1;
        c = 1;
        d = rownanie_kwadratowe.kwadratowe(a, b, c)
        d = np.array(d)
        e = np.roots([a, b, c])
        self.assertNotEqual(d.any(), e.any())

if __name__ == '__main__':
    unittest.main()


