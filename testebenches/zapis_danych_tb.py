from functions import zapis_danych
import unittest

class Safe(unittest.TestCase):
    def test_coding_and_decoding(self):
        basic_code = 174
        #print("Kod poczatkowy:\t", basic_code)
        after_coding = zapis_danych.coding(basic_code)
        after_decoding = zapis_danych.decoding(after_coding)
        #print("Kod po zdekodowaniu:\t", after_decoding)
        self.assertEqual(basic_code, after_decoding)

if __name__ == '__main__':
    unittest.main()