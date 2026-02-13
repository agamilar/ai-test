import pytest
from calculator import add, subtract

@pytest.mark.parametrize('a, b, expected', [
    (1.0, 2.0, 3.0),
    (-1.0, 2.0, 1.0),
    (1.0, -2.0, -1.0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize('a, b, expected', [
    (1.0, 2.0, -1.0),
    (-1.0, 2.0, -3.0),
    (1.0, -2.0, 3.0)
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected