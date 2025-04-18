import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("99/100") == 99
    assert convert("0/5") == 0
    
    with pytest.raises(ValueError):
        convert("2/1")  # Numerator greater than denominator
    with pytest.raises(ValueError):
        convert("abc/5")  # Non-integer input
    with pytest.raises(ValueError):
        convert("4/xyz")  # Non-integer input
    with pytest.raises(ZeroDivisionError):
        convert("1/0")  # Division by zero

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
