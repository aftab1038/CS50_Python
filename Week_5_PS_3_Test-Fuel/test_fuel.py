import pytest
from fuel import convert, gauge

# test valid input
def test_valid():
    assert convert("1/1") == 100 and gauge(100) == "F"
    assert convert("99/100") == 99 and gauge(99) == "F"
    assert convert("1/2") == 50 and gauge(50) == "50%"
    assert convert("1/3") == 33 and gauge(33) == "33%"
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("2/500") == 0 and gauge(0) == "E"

# test ValueError
def test_value_error():
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ValueError):
        convert("5/3")

# test ZeroDivisionError
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
