from lib.exercise_2 import *

def test_encode():
    result = encode("theswiftfoxjumpedoverthelazydog", "secretkey")
    assert result == "EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL"

def test_make_cipher():
    result = make_cipher("secretkey")
    assert result
    