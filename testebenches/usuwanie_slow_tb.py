from functions import usuwanie_slow
import unittest

P = (r'C:\PythonProjekty\Zajecia_Python\pliki\repezytorium.txt')

class Usuwanie(unittest.TestCase):
    def test_after_sie(self):
        list = ["się", "i", "oraz", "nigdy", "dlaczego"]
        list_after = usuwanie_slow.delete(P, list).split(' ')
        #print(list_after)
        self.assertNotIn("się", list_after)
    def test_after_i(self):
        list = ["się", "i", "oraz", "nigdy", "dlaczego"]
        list_after = usuwanie_slow.delete(P, list).split(' ')
        # print(list_after)
        self.assertNotIn("i", list_after)
    def test_after_oraz(self):
        list = ["się", "i", "oraz", "nigdy", "dlaczego"]
        list_after = usuwanie_slow.delete(P, list).split(' ')
        # print(list_after)
        self.assertNotIn("oraz", list_after)
    def test_after_nigdy(self):
        list = ["się", "i", "oraz", "nigdy", "dlaczego"]
        list_after = usuwanie_slow.delete(P, list).split(' ')
        # print(list_after)
        self.assertNotIn("nigdy", list_after)
    def test_after_dlaczego(self):
        list = ["się", "i", "oraz", "nigdy", "dlaczego"]
        list_after = usuwanie_slow.delete(P, list).split(' ')
        # print(list_after)
        self.assertNotIn("dlaczego", list_after)

if __name__ == '__main__':
    unittest.main()
