from lib.exercise_1 import *

def test_hello_kay():
    result = say_hello("kay")
    # print (result)
    assert result == "hello kay"