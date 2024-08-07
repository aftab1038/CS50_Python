from datetime import datetime
import sys

def main():
    DOB = input("Date of Birth: ")
    DOB = validation(DOB)
    print(MinuteCalculation(DOB), "Mintues")
    # print(DOB.year)
    # NOleapYears = leapYear(DOB.year)
    # additionalMint = NOleapYears*24*60
    # print(additionalMint)


def validation(DOB):
    format = "%Y-%m-%d"
    try:
        return datetime.strptime(DOB, format)
        
    except ValueError:
        sys.exit()
    
def leapYear(DOByear):
    leapYears = 0
    currentDate = datetime.now()

    for year in range(DOByear, currentDate.year+1):
        if year%4 == 0:
            leapYears +=1

    return leapYears

def MinuteCalculation(DOB):
    currentDate = datetime.now()
    difference =  currentDate - DOB
    days = difference.days
    minutes = days*24*60
    return minutes


if __name__== "__main__":
    main()


