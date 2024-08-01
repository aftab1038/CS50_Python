import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):
    # search for the youtube link
    # if found then return the link with the new format
    if re.search(r"<iframe(.)*><\/iframe>",s):
        if matches := re.search(r"https?://(?:www\.)?youtube\.com/embed/(\w+)",s, re.IGNORECASE):
            return "https://youtu.be/"+matches[1]

if __name__ == "__main__":
    main()
