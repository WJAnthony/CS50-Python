from um import count

def test_single_words_with_punctuation():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("uM") == 1
    assert count("um?") == 1
    assert count("!@um") == 1
    assert count(".....um   ....") == 1

def test_words_with_um():
    assert count("Album") == 0
    assert count("Petroleum") == 0
    assert count("Magnesium") == 0
    assert count("Aluminum") == 0
    assert count("Incumbent") == 0
    assert count("thumbnail") == 0
    assert count("umbilical") == 0
    assert count("Bumblebee") == 0
    assert count("Ummmmmmm") == 0

def test_short_sentences():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("Um, yeah sure.") == 1
    assert count("yeah, um, i am not sure too.") == 1
    assert count("Um, um, urmm, ummmm um...") == 3
    assert count("thanks, um, jeff.") == 1


