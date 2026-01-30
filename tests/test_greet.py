import greet

def test_greet():
    assert greet.greet('Alice') == 'Hello, Alice!'

def test_greet_empty_name():
    assert greet.greet('') == 'Hello, !'

def test_greet_none():
    assert greet.greet(None) == 'Hello, !'
