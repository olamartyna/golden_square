from lib.check_text_string import *

#Example:
#given a string "drink coffee" = doesn't include TODO so returns False
# Example:
# given a string "#TODO feed the cat" = returns True as it includes #TODO
# Example:
# given a string that only contains "todo" = returns False as not formatted correctly and string incomplete
#Example:
#given string #TODO should return true as it still contains the phrase #TODO

def test_check_no_todo():
    result = check_text_string("drink coffee")
    assert result == False 

def test_check_todo():
    result = check_text_string("#TODO feed the cat")
    assert result == True

def test_check_incomplete_todo():
    result = check_text_string("todo")
    assert result == False

def test_check_only_todo():
    result = check_text_string("#TODO")
    assert result == True
