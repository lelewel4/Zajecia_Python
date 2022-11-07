from functions import hello_world
import unittest

class Helloworld(unittest.TestCase):
    def test_string_correct(self):
        text1 = 'Hello world!'                              #poprawny string
        text2 = hello_world.hello_world_function()
        print(hello_world.hello_world_function())
        self.assertMultiLineEqual(text1, text2)             #unitest do stringow
    def test_string_incorrect(self):
        text1 = 'Test world!'                              #niepoprawny string
        text2 = hello_world.hello_world_function()
        self.assertNotEqual(text1, text2)

if __name__ == '__main__':
    unittest.main()
