import sys
import csv
from tabulate import tabulate


def main():
    # Getting Valid file name by calling function "valid_file()"
    Fname = valid_file()
    # Trying to open the file if found
    try:
        # Dictionary to store the data of csv gile
        menu = []
        # Openning the csv file in read mode
        with open(Fname) as file:
            # adding data row row by csv file to menu dictionary
            reader = csv.reader(file)
            for row in reader:
                menu.append(row)

        # Printing the menu in grid formate
        print(tabulate(menu[1:], headers= menu[0], tablefmt="grid"))

    # if FileNotFoundError araise then  exit by printing "File does not exist"
    except FileNotFoundError:
        sys.exit("File does not exist")

# Function to check for valid command-line arguments
def valid_file():
    # if number of command-line arguments are less than 2
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    # if number of command line-arguments are greater than 2
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    # else if number of command line-arguments are 2
    else:
        # Checking for valid file type, must be ".csv" file
        fname = sys.argv[1]
        # if the sencond argument have extension .csv the return that
        if fname[-4:] == ".csv":
            return fname
        # if not a ".csv" file
        else:
            sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
