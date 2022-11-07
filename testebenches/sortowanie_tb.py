from functions import sortowanie
import random
import unittest

class Sortowanie(unittest.TestCase):
    def test_equal_reverse(self):                                   #poprawny przypadek
        x = random.sample(range(0, 500), 50)
        X1 = x.copy()
        X1.sort(reverse=True)                                       #odwrotnosc sortowania
        X2 = sortowanie.sortowanie(x)
        self.assertEqual(X1, X2)
    def test_equal_normal(self):                                    #niepoprawny przypadek
        x = random.sample(range(0, 500), 50)
        X1 = x.copy()
        X1.sort(reverse=False)                                      #brak odwrotnosci sortowania
        X2 = sortowanie.sortowanie(x)
        self.assertNotEqual(X1, X2)
    def test_empty(self):
        X1 = []                                                     #pusta lista
        X2 = sortowanie.sortowanie(X1)                              #daje znak w konsoli ze lista jest pusta
        self.assertEqual(X1, X2)

if __name__ == '__main__':
    unittest.main()




