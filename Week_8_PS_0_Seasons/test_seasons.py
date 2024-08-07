from seasons import validation

# testing date format
def test_Date():
    assert validation("2006-01-05") == ("2006", "01","05")
    assert validation("january 1, 2024") == None
    assert validation("12,1,2024") == None

