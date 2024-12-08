from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar._capacity == 12
    assert jar._size == 0
    jar = Jar(10)
    assert jar._capacity == 10
    assert jar._size == 0
    jar = Jar(15)
    assert jar._capacity == 15
    assert jar._size == 0
    with pytest.raises(ValueError):
        jar = Jar(-1)
    with pytest.raises(ValueError):
        jar = Jar(-10)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar._size == 1
    jar = Jar()
    jar.deposit(5)
    assert jar._size == 5
    jar = Jar()
    jar.deposit(10)
    assert jar._size == 10
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(15)
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(20)
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(-1)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(1)
    assert jar._size == 11
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(2)
    assert jar._size == 10
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(12)
    assert jar._size == 0
    jar = Jar()
    jar.deposit(12)
    with pytest.raises(ValueError):
        jar.withdraw(15)
    jar = Jar()
    jar.deposit(10)
    with pytest.raises(ValueError):
        jar.withdraw(12)

