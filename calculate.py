from typing import TypeVar, Callable

import re
import operator
from functools import reduce
from collections import deque

T = TypeVar('T')

class Calculator:
    def __init__(self):
        self.ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

    def calculate(self, expr: str) -> float:
        try:
            return self._calculate(expr)
        except ZeroDivisionError:
            raise ValueError('division by zero')
        except Exception as e:
            raise ValueError(f'invalid syntax: {e}')

    def _calculate(self, expr: str) -> float:
        tokens = self._tokenize(expr)
        stack = deque()
        for token in tokens:
            if token in self.ops:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = self.ops[token](operand1, operand2)
                stack.append(result)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    result = self.ops[stack.pop()](operand1, operand2)
                    stack.append(result)
                stack.pop() # pop '('
            else:
                stack.append(float(token))
        return stack.pop()

    def _tokenize(self, expr: str) -> list:
        tokens = re.findall(r'\s*[-+*/()]|\d+\.?\d*', expr)
        return [float(token) if token.isnumeric() else token for token in tokens]

# Usage example
calculator = Calculator()
result = calculator.calculate('(2+3)*4')
print(result)