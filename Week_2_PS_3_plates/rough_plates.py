def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) <= 6 and len(s) >= 2:
        if s.isalnum():
            if s[0:2].isalpha():
                if s[len(s)-1].isdigit():
                    if "0" in s:
                        if s[s.index("0")-1].isalpha():
                            return False
                        else:
                            return True
                    else:
                        return True
        if s.isalpha():
            return True
        

main()