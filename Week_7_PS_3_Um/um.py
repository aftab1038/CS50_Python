import re


def main():
    print(count(input("Text: ")))

def count(s):
    # List that contain all the um
    listUm = re.findall(r"\b\W*um\b\W*", s, re.IGNORECASE)
    
    # return the length of that list 
    return len(listUm)

if __name__ == "__main__":
    main()