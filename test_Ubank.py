# test_bank.py

from Ubank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("hello there") == 0
    assert value("HELLO, Newman") == 0

def test_h_but_not_hello():
    assert value("hey") == 20
    assert value("Hi") == 20
    assert value("howdy") == 20

def test_other():
    assert value("good morning") == 100
    assert value("welcome") == 100
    assert value("bye") == 100
