def main():
    while True:
        try:
            # prompting user to get fraction
            fraction = input("Fraction: ")
            # Converting fraction to percentage
            percentage = convert(fraction)
            # Printing the output E, F or percentage
            print(gauge(percentage))
            break  # break the loop after successful conversion
        except (ValueError, ZeroDivisionError):
            continue  # continue prompting for a valid input

def convert(fraction):
    try:
        # prompting to get input and separate X and Y
        x, y = fraction.split("/")
        # Converting X and Y to integers
        x = int(x)
        y = int(y)

        # Checking if denominator is zero to raise ZeroDivisionError
        if y == 0:
            raise ZeroDivisionError

        # Checking if X is greater than Y, if so raise ValueError
        if x > y:
            raise ValueError

        # else return the fraction or number get after dividing X and Y
        return round((x / y) * 100)

    # if any ValueError or ZeroDivisionError, then raise again
    except (ValueError, ZeroDivisionError) as e:
        raise e

def gauge(percentage):
    # If, though, 1% or less remains, return E instead to indicate that the tank is essentially empty
    if percentage <= 1:
        return "E"
    # If 99% or more remains, return F instead to indicate that the tank is essentially full
    elif percentage >= 99:
        return "F"
    # Else return the percentage of fuel in tank
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()
