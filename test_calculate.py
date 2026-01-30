import unittest
from calculate import Calculator

class TestCalculator(unittest.TestCase):

    def test_precedence(self):
        calculator = Calculator()
        self.assertEqual(calculator.calculate('2+3*4'), 14.0)

    def test_parentheses(self):
        calculator = Calculator()
        self.assertEqual(calculator.calculate('(2+3)*4'), 20.0)

    def test_unary_minus(self):
        calculator = Calculator()
        self.assertEqual(calculator.calculate('-3*2'), -6.0)
        self.assertEqual(calculator.calculate('2*-3'), -6.0)

    def test_floats(self):
        calculator = Calculator()
        self.assertEqual(calculator.calculate('3.5*2'), 7.0)

    def test_invalid_syntax(self):
        with self.assertRaises(ValueError) as context:
            Calculator().calculate('2++2')
        self.assertEqual(str(context.exception), 'invalid syntax: 2++2')

    def test_division_by_zero(self):
        with self.assertRaises(ValueError) as context:
            Calculator().calculate('2/0')
        self.assertEqual(str(context.exception), 'division by zero')

if __name__ == '__main__':
    unittest.main()