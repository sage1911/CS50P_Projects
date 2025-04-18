import pytest
from plates import is_valid

def test_length():
    assert is_valid("A") == False
    assert is_valid("AA") == True
    assert is_valid("AAAAAAA") == False

def test_start_letters():
    assert is_valid("1A") == False
    assert is_valid("A1") == False
    assert is_valid("AB1234") == True

def test_number_placement():
    assert is_valid("AB12CD") == False
    assert is_valid("AB1234") == True
    assert is_valid("AB0123") == False

def test_valid_characters():
    assert is_valid("AB12!@") == False
    assert is_valid("AB 123") == False
    assert is_valid("AB123") == True
