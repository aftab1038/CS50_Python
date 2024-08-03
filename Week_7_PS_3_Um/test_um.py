from um import count


# testing with different cases upper lower and mix
def test_diffCase():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("Hello UM, world") == 1
    assert count("um") == 1

# testing word with letter um
def test_withoutUM():
    assert count("Hello, world") == 0
    assert count("Yummy food") == 0
    assert count("The mummy movie ") == 0

# testing with symbols 
def test_withSymbols():
    assert count("um!") == 1
    assert count("hello um, um!") == 2
    assert count("um...") == 1
    assert count(" um  UM ") == 2