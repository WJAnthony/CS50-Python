from plates import is_valid

def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("ECTO88") == True
    assert is_valid("NRVOUS") == True

def test_first_digit_0():
    assert is_valid("CS05") == False
    assert is_valid("50") == False

def test_ends_with_alphabet():
    assert is_valid("CS50P") == False

def test_contains_punctuations():
    assert is_valid("PI3.45") == False

def test_too_short():
    assert is_valid("H") == False

def test_too_long():
    assert is_valid("BALLLLLLLLLLLL") == False

def test_alphabet_sandwich():
    assert is_valid("CS50P2") == False

def test_first_2_alphabets():
    assert is_valid("C9000") == False
    assert is_valid("H") == False
    assert is_valid("2") == False
    assert is_valid("50") == False

