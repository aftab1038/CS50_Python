from response import email_validation

# testing valid emails
def test_valid():
    assert email_validation("malan@harvard.edu") == "Valid"
    assert email_validation("aftabk.1038@gmail.com") == "Valid"
    assert email_validation("aftabk.1038@outlook.com") == "Valid"
  
# testing invalid emails
def test_invalid():
    assert email_validation("malan@@@harvard.edu") == "Invalid"
    assert email_validation("aftabk.1038@gmail...com") == "Invalid"
    assert email_validation("aftabk.1038") == "Invalid"