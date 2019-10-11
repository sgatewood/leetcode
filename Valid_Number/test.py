from vn import valid_number
import unittest

good = ["0"," 0.1 ","2e10"," -90e3   "," 6e-1","53.5e93",".1","3."]
bad = ["abc","1 a"," 1e","e3"," 99e2.5 "," --6 ","-+3","95a54e53"]

class TestLPS(unittest.TestCase):

    def test_good(self):
        for e in good:
            self.assertTrue(valid_number(e),"%r" % e)

    def test_bad(self):
        for e in bad:
            self.assertFalse(valid_number(e),"%r" % e)

if __name__ == '__main__':
    unittest.main()
