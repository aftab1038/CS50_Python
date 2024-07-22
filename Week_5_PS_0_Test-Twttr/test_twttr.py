from twttr import shorten

# Testing Different cases words lower, upper and mix
def test_cases():
    assert shorten("twitter") == "twttr"
    assert shorten("AFTAB") == "FTB"
    assert shorten("DavId MaLAn") == "Dvd MLn"

# testing numbers
def test_number():
    assert shorten("50") == "50"
    assert shorten("0.50") == "0.50"
    assert shorten("2024") == "2024"

# Testing punctuation
def test_punctuation ():
    assert shorten("!@#$") == "!@#$"
    assert shorten("%^&*.?") == "%^&*.?"
    assert shorten("{]~`") == "{]~`"
