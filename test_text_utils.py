import pytest
from text_utils import count_words

@pytest.mark.parametrize('text, expected', [
    ('Hello world', 2),
    ('  Python   is   great ', 3),
    ('One', 1),
    ('', 0),
    ('   ', 0)
])
def test_count_words(text, expected):
    assert count_words(text) == expected