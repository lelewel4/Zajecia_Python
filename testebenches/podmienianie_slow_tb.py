from functions import podmienianie_slow
import unittest

P = (r'C:\PythonProjekty\Zajecia_Python\pliki\repezytorium.txt')

class Podmiana(unittest.TestCase):
    def test_compatible_table_size(self):                               #sprawdzenie czy da sie wszytsko podmienic
        list_del_len = len(["się", "i", "oraz", "nigdy", "dlaczego"])
        list_rep_len = len(["oraz", "i", "prawie", "nigdy", "czemu"])
        self.assertEqual(list_rep_len, list_del_len)
    def test_after_sie(self):
        list_del = ["się", "i", "oraz", "nigdy", "dlaczego"]
        list_rep = ["oraz", "i", "prawie", "nigdy", "czemu"]
        list_after = podmienianie_slow.replace(P, list_del, list_rep)
        list_after = list_after.split(' ')
        self.assertNotIn("się", list_after)
    def test_after_dlaczego(self):
        list_del = ["się", "i", "oraz", "nigdy", "dlaczego"]
        list_rep = ["oraz", "i", "prawie", "nigdy", "czemu"]
        list_after = podmienianie_slow.replace(P, list_del, list_rep)
        list_after = list_after.split(' ')
        # print(list_after)
        self.assertNotIn("dlaczego", list_after)

if __name__ == '__main__':
    unittest.main()