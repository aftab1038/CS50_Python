from datetime import datetime
import inflect
import sys

def main():
    p = inflect.engine()

    # taking input 
    DOB = input("Date of Birth: ")
    # checking the formate of date YY-MM-DD
    
    DOB = validation(DOB)
    # Calculating minutes 
    Minutes = MinuteCalculation(DOB)
    # minutes in words
    MintuesInWords = p.number_to_words(Minutes).replace(" and ", " ")
    # printing minutes 
    print(MintuesInWords, "minutes")

# Functiin for checking the format of date inputted  
def validation(DOB):
    # Defining format
    format = "%Y-%m-%d"
    # Checking the date 
    try:
        # if valid date then returning the date 
        return datetime.strptime(DOB, format)
    # if invalid date then exit 
    except ValueError:
        sys.exit("Invalid date")

# Calculating mintues 
def MinuteCalculation(DOB):
    # current date 
    currentDate = datetime.now()
    # difference between current and date of birth, return the days 
    difference =  currentDate - DOB
    days = difference.days
    # converting days to mmintues and return mintues  
    minutes = days*24*60
    return minutes


if __name__== "__main__":
    main()


