from functions import mnozenie_macierzy
import numpy as np
import unittest

class Macierze(unittest.TestCase):
    def test_compatible_array_size(self):  # sprawdzenie czy da sie wymnozyc macierz
        a = np.array([[2, 1, 3], [-1, 4, 0]])
        b = np.array([[1, 3, 2], [-2, 0, 1], [5, -3, 2]])
        a_size = a.shape[1]
        b_size = b.shape[0]
        #print("Row size: ", a_size, "\nColumn size: ", b_size, '\n')
        self.assertEqual(a_size, b_size)
    def test_equal_multiple_correct(self):  # sprawdzenie poprawnosci wlasnej funkcji
        a = np.array([[2, 1, 3], [-1, 4, 0]])
        b = np.array([[1, 3, 2], [-2, 0, 1], [5, -3, 2]])
        c = mnozenie_macierzy.mnozenie(a, b).all()
        d = np.matmul(a, b, dtype=float).all()
        #print(mnozenie_macierzy.mnozenie(a, b))
        self.assertEqual(c, d)

if __name__ == '__main__':
    a = np.array([["s", "s", "s"], ["s", "s", "s"]])                        #zwroci blad
    b = np.array([["s", "s", "s"], ["s", "s", "s"], ["s", "s", "s"]])
    mnozenie_macierzy.mnozenie(a, b)

    unittest.main()
