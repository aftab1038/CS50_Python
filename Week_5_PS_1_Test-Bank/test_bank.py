from bank import value

# Testing upper Case Greeting
def test_upperCaseGreet():
    assert value("HELLO, THIS IS CS50!") == 0
    assert value("HI, THIS IS CS50!") == 20
    assert value("THIS IS CS50!") == 100

# Testing lower Case Greeting
def test_lowerCaseGreet():
    assert value("hello, this is cs50!") == 0
    assert value("hi, this is cs50!") == 20
    assert value("this is cs50!") == 100

# Testing mix Case Greeting
def test_mixCaseGreet():
    assert value("HeLlO, tHiS Is Cs50!") == 0
    assert value("hI, ThiS Is cS50!") == 20
    assert value("THis Is CS50!") == 100
