import pytest
from work import convert

def test_valid_times():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"

def test_invalid_times():
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")  # Invalid hour
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")  # Invalid minute
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")  # Missing "to"
    with pytest.raises(ValueError):
        convert("9:00 to 5:00")  # Missing AM/PM
    with pytest.raises(ValueError):
        convert("hello world")  # Completely invalid string

