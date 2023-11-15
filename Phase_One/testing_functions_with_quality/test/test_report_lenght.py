from lib.report_length import *

def test_string_length():
    result = report_length('laptop')
    assert result == "This string was 6 characters long."