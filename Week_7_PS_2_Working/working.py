import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # checking for correct format
    format = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s, re.IGNORECASE)
    # if true formate found in format
    if format:
        parts = format.groups()
        # hours cannot be greater than 12  
        if int(parts[1])>12 or int(parts[5])>12:
            raise ValueError
        
        # converting time to new format
        firstTime = formatting(parts[1],parts[2],parts[3])
        secondTime = formatting(parts[5],parts[6],parts[7])
        return firstTime+ " to " +secondTime
    
    # if true formate not found in format
    else:
       raise ValueError 

def formatting (hour, minute, am_pm):
    # formatting hours A/C to am and pm
    # if its pm
    if am_pm == "PM":
        # 12pm is 12 
        if int(hour) == 12:
            newHours = 12
        # 1 pm = 13 converting A/C to this
        else:
            newHours = int(hour)+12
    # if its am 
    else:
        # 12am is 00 
        if int(hour) == 12:
            newHours = 0
        # 1am is 1  converting A/C to this
        else:
            newHours = int(hour)

    # formatting minutes
    # if minute is not entered that mean 0
    if minute ==  None:
        newMinute = ":00"
        # time = hours : minute
        newTime = str(f"{newHours:02}")+newMinute
    # if minutes entered:
    else:
        # time = hours : minute
        newTime = str(f"{newHours:02}")+":"+minute

    # returning the new formatted time
    return newTime

if __name__ == "__main__":
    main()