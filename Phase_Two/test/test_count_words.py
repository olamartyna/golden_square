from lib.count_words import *

def test_one_word():
    result = count_words('cat')
    assert result == 1

def test_more_words():
    result = count_words('The above is a simplified approach. Over time you will add more techniques to it.')
    assert result == 15

def test_empty_string():
    result = count_words(' ')
    assert result == 0

def test_one_character():
    result = count_words('a')
    assert result == 1

def test_spaces_around():
    result = count_words('  a  ')
    assert result == 1

def test_many_spaces_between():
    result = count_words('spacious   space')
    assert result == 2