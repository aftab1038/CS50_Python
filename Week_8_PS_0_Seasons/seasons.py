from datetime import date
import re
import inflect
import sys

p = inflect.engine()

def main():
    # taking input
    DOB = input("Date of Birth: ")
    # checking the format of date YYYY-MM-DD
    try:
        year, month, day = validation(DOB)
        birthDate = date(int(year), int(month), int(day))
    except:
        sys.exit("Invalid Date")

    # current date
    currentDate = date.today()
    # difference between current date and date of birth, return the days
    difference = currentDate - birthDate
    days = difference.days
    # converting days to minutes and return minutes
    minutes = days * 24 * 60
    # minutes in words
    MinutesInWords = p.number_to_words(minutes).replace(" and ", " ")
    # printing minutes
    print(MinutesInWords.capitalize(), "minutes")

# Function for checking the format of date inputted
def validation(DOB):
    if re.search(r"^\d{4}-\d{2}-\d{2}$", DOB):
        year, month, day = DOB.split("-")
        return year, month, day

if __name__ == "__main__":
    main()
