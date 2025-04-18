import pytest

from convert import convert

def test_conversion():
    assert convert(1) == 149597870700