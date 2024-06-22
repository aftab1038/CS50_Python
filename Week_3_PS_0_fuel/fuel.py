# Main function
def main():
    # prompting user to get fraction
    fraction = get_fraction("Fraction: ")
    # Converting the fraction to percentage 
    percentage = round(fraction*100)

    # If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty
    if percentage <= 1:
        print("E")
    # If 99% or more remains, output F instead to indicate that the tank is essentially full
    elif percentage >= 99:
        print("F")
    # Else output the percentage of fuel in tank 
    else:
        print(percentage, "%", sep="")


# Defining get_fraction() function, to get valid input (fraction) 
def get_fraction(prompt):
    # looping untill user enter valid fraction
    while True:
        # try untill we get fraction -formatted as X/Y
        try:
            # prompting to get input and seperate X and Y
            x, y = input(prompt).split("/")
            # Converting X and Y to integers
            x = int(x)
            y = int(y)
            # Checking if X is greater or not, if is it not error raise ValueError
            if x>y:
                raise ValueError
            #else return the fraction or number get after dividing X and Y
            else:
                return (x/y)

        # if any ValueError or ZeroDivisionError, then loop again
        except (ValueError, ZeroDivisionError):
            pass


# Calling main function
main()