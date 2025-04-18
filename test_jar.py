from jar import Jar
import pytest

def test_init():
    """Test valid and invalid jar initialization"""
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0  # Jar starts empty
    
    with pytest.raises(ValueError):  # Negative capacity should fail
        Jar(-1)
    
    with pytest.raises(TypeError):  # Non-integer capacity should fail
        Jar("big")

def test_str():
    """Test string representation of the jar"""
    jar = Jar(5)
    assert str(jar) == ""  # Empty jar

    jar.deposit(2)
    assert str(jar) == "🍪🍪"

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪🍪"

def test_deposit():
    """Test adding cookies to the jar"""
    jar = Jar(5)
    
    jar.deposit(3)
    assert jar.size == 3  # Should have 3 cookies now
    
    with pytest.raises(ValueError):  # Adding beyond capacity should fail
        jar.deposit(3)

    with pytest.raises(ValueError):  # Negative deposits should fail
        jar.deposit(-2)

def test_withdraw():
    """Test removing cookies from the jar"""
    jar = Jar(5)
    jar.deposit(4)
    
    jar.withdraw(2)
    assert jar.size == 2  # Should have 2 cookies left

    with pytest.raises(ValueError):  # Can't remove more than available
        jar.withdraw(5)

    with pytest.raises(ValueError):  # Negative withdrawal should fail
        jar.withdraw(-1)
