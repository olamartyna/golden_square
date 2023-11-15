# from lib.reminder import *

# def test_reminder():
#     reminder = Reminder("Kay")
#     result = reminder.remind()
#     assert result == "No reminder set!"


import pytest # <-- New code
from lib.reminder import *


def test_reminder():
    reminder = Reminder("Kay")
    with pytest.raises(Exception) as e: # <-- New code
        reminder.remind()
    error_message = str(e.value) # <-- New code
    assert error_message == "No reminder set!"