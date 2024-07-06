import unittest

from one import addTwo, subtract, multiply, divide, helloPythonTesting

class testBasicFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(addTwo(1,2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(1,2), -1)

    def test_multiply(self):
        self.assertEqual(multiply(2,3), 6)

    def test_divide(self):
        self.assertEqual(divide(9,3),3)

    def test_print(self):
        self.assertEqual(helloPythonTesting(), None)

if __name__ == "__main__":
    unittest.main()