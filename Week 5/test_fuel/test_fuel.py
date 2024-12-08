from fuel import convert, gauge
import pytest

def test_XandY_not_int():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_X_greater_than_Y():
    with pytest.raises(ValueError):
        convert("4/3")

def test_Y_equals_0():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_full():
    assert convert("4/4") == 100
    assert convert("99/100") == 99
    assert gauge(100) == "F"
    assert gauge(99) == "F"

def test_empty():
    assert convert("0/4") == 0
    assert convert("1/100") == 1
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_valid():
    assert convert("1/3") == 33
    assert convert("2/3") == 67
    assert convert("3/4") == 75
    assert gauge(33) == "33%"
    assert gauge(67) == "67%"
    assert gauge(75) == "75%"


