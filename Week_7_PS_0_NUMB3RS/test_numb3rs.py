import pytest
from numb3rs import validate

# testing valid ip
def test_True():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True

# testing invalid ip
def test_False():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
