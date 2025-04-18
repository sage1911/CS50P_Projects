from numb3rs import validate

def test_valid_ips():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True

def test_invalid_ips():
    assert validate("275.3.6.28") == False  # Invalid octet > 255
    assert validate("-1.2.3.4") == False  # Negative number
    assert validate("256.256.256.256") == False  # Octet out of range
    assert validate("192.168.1") == False  # Missing octet
    assert validate("192.168.1.1.1") == False  # Extra octet
    assert validate("192.168.one.1") == False  # Non-numeric values
    assert validate("192.168.01.1") == True  # Leading zeros should be allowed

def test_edge_cases():
    assert validate("") == False  # Empty string
    assert validate("...1") == False  # Incomplete address
    assert validate("1234.1.1.1") == False  # Octet too large
