import pytest
import calculator

@pytest.mark.parametrize('a, b, expected', [
    (1.0, 2.0, 3.0),
    (-1.0, 2.0, 1.0),
    (1.5, 2.5, 4.0)
])
def test_add(a, b, expected):
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize('a, b, expected', [
    (1.0, 2.0, -1.0),
    (-1.0, 2.0, -3.0),
    (1.5, 2.5, -1.0)
])
def test_subtract(a, b, expected):
    assert calculator.subtract(a, b) == expected