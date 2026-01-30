import unittest
from utils import utils

class TestUtils(unittest.TestCase):
    def test_example_function(self):
        self.assertEqual(utils.example_function(1, 'test'), '1test')

if __name__ == '__main__':
    unittest.main()