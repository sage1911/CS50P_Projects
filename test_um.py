import pytest
from um import count

def test_single_um():
    assert count("um") == 1
    assert count("um,") == 1
    assert count("um.") == 1
    assert count("um!") == 1
    assert count("Um") == 1  # Case insensitive

def test_multiple_um():
    assert count("um um um") == 3
    assert count("Um, um, um!") == 3
    assert count("Um. Ummm um.") == 2

def test_um_inside_words():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("album") == 0

def test_um_with_spacing():
    assert count(" um ") == 1
    assert count("  um um  ") == 2
    assert count("\tum\tum\t") == 2

def test_no_um():
    assert count("hello world") == 0
    assert count("U M") == 0
