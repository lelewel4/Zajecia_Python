from functions import konwersja_rozszerzenia
import unittest

class Konwersja(unittest.TestCase):
    def test_file_extension_before(self):
        P = (r'C:\Users\label\Dropbox\Mój komputer (LAPTOP-BHUGETIH)\Desktop\python_zad6\plik1test.jpg')
        text1 = P[-4:]                      #".jpg"
        text2 = '.jpg'
        self.assertEqual(text1, text2)
    def test_file_extension_after(self):
        P1 = (r'C:\Users\label\Dropbox\Mój komputer (LAPTOP-BHUGETIH)\Desktop\python_zad6\plik1test.jpg')
        konwersja_rozszerzenia.convert_jpg_to_png(P1)
        P2 = (r'C:\Users\label\Dropbox\Mój komputer (LAPTOP-BHUGETIH)\Desktop\python_zad6\plik1test.png')
        text1 = P2[-4:]                      #".png"
        text2 = '.png'
        self.assertEqual(text1, text2)

if __name__ == '__main__':
    unittest.main()