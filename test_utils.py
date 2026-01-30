import unittest
from utils import is_palindrome

class TestUtils(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))

if __name__ == "__main__":
    unittest.main()
