from working import convert
import pytest

def test_single_digits():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 AM to 4 PM") == "10:00 to 16:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("9 PM to 8 AM") == "21:00 to 08:00"
    assert convert("8 PM to 10 AM") == "20:00 to 10:00"
    assert convert("10 PM to 11 AM") == "22:00 to 11:00"

def test_double_digits():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:00 AM to 4:00 PM") == "10:00 to 16:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("9:00 PM to 8:00 AM") == "21:00 to 08:00"
    assert convert("8:00 PM to 10:00 AM") == "20:00 to 10:00"
    assert convert("10:00 PM to 11:00 AM") == "22:00 to 11:00"

def test_mixed_digits():
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 4:00 PM") == "10:00 to 16:00"
    assert convert("8:00 AM to 6 PM") == "08:00 to 18:00"
    assert convert("9:00 PM to 8 AM") == "21:00 to 08:00"
    assert convert("8 PM to 10:00 AM") == "20:00 to 10:00"
    assert convert("10:00 PM to 11 AM") == "22:00 to 11:00"

def test_Invalid_time():
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 13:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM - 6:00 PM")
    with pytest.raises(ValueError):
        convert("9AM - 6 PM")
