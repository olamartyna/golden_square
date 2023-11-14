from lib.gratitudes import *

def test_gratitudes():
    gratitude = Gratitudes()
    gratitude.add('dog')
    result = gratitude.format()
    assert result == "Be grateful for: dog"

    gratitude.add('cat')
    result = gratitude.format()
    assert result == "Be grateful for: dog, cat"
