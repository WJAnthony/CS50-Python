from numb3rs import validate


def test_all_valid():
    assert validate("0.0.0.0") == True
    assert validate("1.1.1.1") == True
    assert validate("255.255.255.255") == True
    assert validate("127.36.111.87") == True

def test_one_invalid():
    assert validate("512.0.0.1") == False
    assert validate("0.444.0.1") == False
    assert validate("0.0.369.1") == False
    assert validate("0.0.0.256") == False

def test_multiple_invalid():
    assert validate("500.500.500.501") == False
    assert validate("500.5.500.501") == False
    assert validate("-5.39.60.50") == False

def test_invalid_input():
    assert validate("cat") == False
    assert validate("dog") == False
    assert validate("hello") == False
