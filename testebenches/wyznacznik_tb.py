from functions import wyznacznik
import numpy as np
import unittest

class Wyznacznik(unittest.TestCase):
    def test_one_element(self):                                 #macierz 1x1
        A = np.array([[1, 0, 5], [3, 0, 6], [-7, 8, 6]])
        self.assertNotEqual(len(A), "1")
    def test_square_size(self):                                 #kwadartowa macierz
        A = np.array([[1, 0, 5], [3, 0, 6], [-7, 8, 6]])
        num_rows = len(A)
        num_cols = len(A[0])
        self.assertEqual(num_cols, num_rows)
    def chech_function(self):                                   #poprawny wynik
        A = np.array([[1, 0, 5], [3, 0, 6], [-7, 8, 6]])
        detA1 = np.linalg.det(A)
        detA2 = wyznacznik.matrix_determinant(A)
        self.assertEqual(detA1, detA2)

if __name__ == '__main__':
    unittest.main()
