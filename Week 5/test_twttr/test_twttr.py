from twttr import shorten

def test_capitalise():
    assert shorten("HELLO APPLE ITU") == "HLL PPL T"

def test_normal():
    assert shorten("twitter") == "twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_no_vowels():
    assert shorten("CS50") == "CS50"

