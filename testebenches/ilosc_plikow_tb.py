from functions import ilosc_plikow
import unittest

class Liczenie(unittest.TestCase):
    def test_equal_count_correct(self):
        X1 = ilosc_plikow.liczenie("../venv/Lib/site-packages")            #sciezka do pliku
        X2 = 21                                                            #liczba plikow jaka znajduje w katologu
        self.assertEqual(X1, X2)                                           #unitest do porownania dwoch wartosci
    def test_equal_count_incorrect(self):
        X1 = ilosc_plikow.liczenie("../venv/Lib/site-packages")            #sciezka do pliku
        X2 = 105                                                           #niepoprawna liczba plikow jaka znajduje w katologu
        self.assertNotEqual(X1, X2)

if __name__ == '__main__':
    unittest.main()
