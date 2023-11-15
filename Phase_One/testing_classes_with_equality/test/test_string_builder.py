from lib.string_builder import *

def test_building_the_string():
    str_builder = StringBuilder()
    str_builder.add('dog')
    result = str_builder.output()
    assert result == 'dog'

def test_string_length():
    str_size = StringBuilder()
    str_size.add('lemur')
    result = str_size.size()
    assert result == 5