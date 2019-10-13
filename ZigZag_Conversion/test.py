from convert import convert
import unittest

class TestConvert(unittest.TestCase):

    def test_example_1(self):
        actual = convert("PAYPALISHIRING",3)
        expected = "PAHNAPLSIIGYIR"
        self.assertEqual(actual,expected)

    def test_example_2(self):
        actual = convert("PAYPALISHIRING",4)
        expected = "PINALSIGYAHRPI"
        self.assertEqual(actual,expected)

    def test_1(self):
        actual = convert("123456789",1)
        expected = "123456789"
        self.assertEqual(actual,expected)

    def test_2(self):
        actual = convert("123456789",2)
        expected = "135792468"
        self.assertEqual(actual,expected)

    def test_3(self):
        actual = convert("123456789",3)
        expected = "159246837"
        self.assertEqual(actual,expected)

if __name__ == '__main__':
    unittest.main()
