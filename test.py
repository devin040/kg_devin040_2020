import unittest
from main import str_map

"""
For clarity:
    0 = True
    1 = False
"""

class TestStringMapping(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(str_map("foo", "bar"), 1)
        self.assertEqual(str_map("bar", "foo"), 0)
        self.assertEqual(str_map("abc", "bcd"), 0)
        self.assertEqual(str_map("123", "321"), 0)
        self.assertEqual(str_map("barr", "fldd"), 0)
        self.assertEqual(str_map("barr", "fldi"), 1)

    # This test is of the assumption that provided each character in s1
    # maps to exactly one character in s2, print true.
    # Does not prohibit a character in s2 from having no mapping to s1
    def test_diff_len(self):
        self.assertEqual(str_map("123", "1234"), 0)
        self.assertEqual(str_map("bard", "foo"), 1)
        self.assertEqual(str_map("bar", "foooooo"), 0)
        self.assertEqual(str_map("12333", "123"), 0)
        self.assertEqual(str_map("123334", "123"), 1)

    def test_special_chars(self):
        self.assertEqual(str_map("$%^", "$%^"), 0)
        self.assertEqual(str_map("$$^", "&*("), 1)
        self.assertEqual(str_map("bar a", "fod 2"), 1)
        self.assertEqual(str_map("bar a", "fod o"), 0)

    def test_case(self):
        self.assertEqual(str_map("foO", "bar"), 1)
        self.assertEqual(str_map("bar", "foO"), 0)

if __name__ == '__main__':
    unittest.main()
