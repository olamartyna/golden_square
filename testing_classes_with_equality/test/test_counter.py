from lib.counter import *

def test_self_counter():
    counter = Counter()
    counter.add(4)
    result = counter.report()
    assert result == "Counted to 4 so far."