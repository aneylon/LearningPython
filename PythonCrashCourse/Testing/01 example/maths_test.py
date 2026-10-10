import maths

# print(maths.add(1,2))
# print(maths.subtract(1,2))
# print(maths.multiply(1,2))
# print(maths.divide(1,2))

import unittest

class TestMathsFunctions(unittest.TestCase) :
    def test_add(self) :
        self.assertEqual(maths.add(1,2), 3)

    def test_subtract(self) :
        self.assertEqual(maths.subtract(1,2), -1)

    def test_multiply(self) :
        self.assertEqual(maths.multiply(1,2), 2)

    def test_divide(self) : 
        self.assertEqual(maths.divide(1,2), 0.5)

if __name__ == "__main__" :
    unittest.main()
