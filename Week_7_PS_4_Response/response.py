from validator_collection import validators
import sys

def main():
    print(email_validation(input("What's your email address? ")))

def email_validation(email):
    # checking for valid 
    try:
        # if email is in valid format print valid
        email_address = validators.email(email)
        return "Valid"
    except:
        # else sys.exit with invalid messages
        return "Invalid"
    
if __name__ == "__main__":
    main()