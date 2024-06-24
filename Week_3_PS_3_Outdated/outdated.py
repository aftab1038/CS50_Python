# Month list
month = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
]

# Asking untill a valid input entered by user
while True:
    try:
        date = input("Date: ").title()

        # if this formate 2/2/1800 of date entered by user
        if "/" in date:
            M, D, Y = date.split("/")
            D = int(D.strip())
            M = int(M.strip())
            Y = int(Y.strip())

            # Checking for valid date and valid month
            if M>12 or D>31:
                raise ValueError
            # printing the date in year-month-day (YYYY-MM-DD) formate
            print(f"{Y}-{M:02}-{D:02}")

        # Or if this formated August 9, 1636 of date entered by user
        elif "," in date:
            MD, Y = date.split(",")
            M, D = MD.split(" ")
            D = int(D.strip())
            M = M.strip()
            M = month.index(M)+1
            Y = int(Y.strip())
            
            # Checking for valid date and valid month
            if M>12 or D>31:
                raise ValueError
            # printing the date in year-month-day (YYYY-MM-DD) formate
            print(f"{Y}-{M:02}-{D:02}")

        # Any date formate other than above 2, raise ValueError
        else:
            raise ValueError

        # Break the loop is no error araise
        break

    # If ValueError raise, continue loop
    except ValueError:
        continue
