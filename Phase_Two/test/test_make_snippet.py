from lib.make_snippet import *

# Funtion needs to take a string:
# 1. If it's under 5 words - return the first 5 words and '...'
# 2. If it's less than 5 words - return the whole string 
def test_if_short_string_returned():
    result_1 = make_snippet('cat')
    assert result_1 == 'cat'

    result_2 = make_snippet('You may immediately think I know how to code that!')
    assert result_2 == 'You may immediately think I...'