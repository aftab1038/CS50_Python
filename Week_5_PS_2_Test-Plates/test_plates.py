from plates import is_valid

# Testing valid plates
def test_validPlate():
    assert is_valid("CS50") == True
    assert is_valid("GIL450") == True
    assert is_valid("ABC123") == True

# Testing invalid plates
def test_invalidPlate():
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("lahore1") == False
