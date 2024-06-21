def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # vanity plates may contain a maximum of 6 characters
    if len(s) <= 6 and len(s) >= 2:
        # All vanity plates contain letters or numbers only -periods, spaces, or punctuation marks are not allowed
        if s.isalnum():
            # All vanity plates must start with at least two letters
            if s[0:2].isalpha():
                # Numbers cannot be used in the middle of a plate; they must come at the end. - valid format "AAA222"
                # The first number used cannot be a ‘0’.”
                for char in s:
                    if char.isdigit():
                        index = s.index(char)
                        if s[index:].isdigit() and char != "0":
                            return True
                        else:
                            return False
                # Return true if all the character are letters
                return True


main()