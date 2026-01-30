import unittest
from src.hello import hello

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello('Alice'), 'Hello, Alice!')
        self.assertEqual(hello('Bob'), 'Hello, Bob!')

if __name__ == '__main__':
    unittest.main()