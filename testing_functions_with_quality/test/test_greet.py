from lib.greet import *

def test_greet_returns_hello_bob():
    result = greet('Bob')
    assert result == 'Hello, Bob!'