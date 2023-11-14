from lib.check_codeword import *

def test_check_horse():
    result = check_codeword('horse')
    assert result == "Correct! Come in."

def test_check_letters():
    result = check_codeword('house')
    assert result == "Close, but nope."

def test_check_wrong():
    result = check_codeword('dog')
    assert result == "WRONG!"