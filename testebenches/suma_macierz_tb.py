from functions import suma_macierzy
import numpy as np
import unittest

class Dodawanie(unittest.TestCase):
    def test_compatible_array_size(self):                               #sprawdzenie czy da sie wymnozyc macierz
        A = np.random.rand(2, 2)
        B = np.random.rand(2, 2)
        A_size = A.shape
        B_size = B.shape
        self.assertEqual(A_size, B_size)
    def test_add_matrix(self):
        A = np.random.rand(2, 2)
        B = np.random.rand(2, 2)
        #print(suma_macierzy.suma_macierzy(A, B))
        self.assertEqual(suma_macierzy.suma_macierzy(A, B).all(), np.add(A, B).all())

if __name__ == '__main__':
    unittest.main()
