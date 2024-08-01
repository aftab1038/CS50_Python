import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Checking the format of ip
    if re.match(r"^\d+\.\d+\.\d+\.\d+$", ip):
        # Splitting numbers
        listNUM = ip.split(".")
        # Checking numbers are in between 255 and 0
        for NUM in listNUM:
            # if any number is not in the valid range, return False immediately
            if not (0 <= int(NUM) <= 255):
                return False
        # if all numbers are valid, return True
        return True
    # For invalid format of ip, return False
    return False

if __name__ == "__main__":
    main()
