from twttr import shorten

def test_lowercase():
    assert shorten("hello") == "hll"
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("HELLO") == "HLL"
    assert shorten("TWITTER") == "TWTTR"

def test_mixed_case():
    assert shorten("HeLLo") == "HLL"
    assert shorten("TwItTeR") == "TwtTR"

def test_numbers():
    assert shorten("1234") == "1234"
    assert shorten("h3ll0") == "h3ll0"

def test_symbols():
    assert shorten("!@#$%^&*()") == "!@#$%^&*()"
    assert shorten("c0d!ng") == "c0d!ng"

def test_empty_string():
    assert shorten("") == ""

def test_only_vowels():
    assert shorten("aeiouAEIOU") == ""

def test_sentences():
    assert shorten("I love Python!") == " lv Pythn!"
