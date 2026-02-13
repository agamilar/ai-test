# test_calculator.py

import pytest
from calculator import add, subtract

def test_add():
    assert add(1.0, 2.0) == 3.0
    assert add(-1.0, 1.0) == 0.0
    assert add(0.0, 0.0) == 0.0

def test_subtract():
    assert subtract(1.0, 2.0) == -1.0
    assert subtract(-1.0, 1.0) == -2.0
    assert subtract(0.0, 0.0) == 0.0