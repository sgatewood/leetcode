from lps import lps
import unittest

class TestLPS(unittest.TestCase):

    def test_example_1(self):
        actual = lps("babad")
        self.assertTrue(actual in ("bab","aba"))

    def test_example_2(self):
        actual = lps("cbbd")
        expected = "bb"
        self.assertEqual(actual,expected)

    def test_palindrome(self):
        actual = lps("racecar")
        expected = "racecar"
        self.assertEqual(actual,expected)

    def test_empty(self):
        actual = lps("")
        expected = ""
        self.assertEqual(actual,expected)

    def test_one(self):
        actual = lps("")
        expected = ""
        self.assertEqual(actual,expected)

if __name__ == '__main__':
    unittest.main()
