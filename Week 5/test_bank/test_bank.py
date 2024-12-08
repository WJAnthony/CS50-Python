from bank import value

def test_hello():
    assert value("Hello") == int(0)

def test_name():
    assert value("Hello, Newman") == int(0)

def test_starts_with_h():
    assert value("How you doing?") == int(20)

def test_no_h():
    assert value("What's happening?") == int(100)

def test_spacing_before_and_after():
    assert value("    Hello    ") == int(0)
