import sys
import csv

def main():
    # Getting Valid file names by calling function "valid_file()"
    before, after = valid_file()
    # Trying to open the file if found
    try:
        # Dictionary to store the data of csv file
        data = []
        # Dictionary to store the modified data of csv file
        modData = []
        # Openning the csv file in read mode
        with open(before) as file:
            # adding data row row by csv file to menu dictionary
            reader = csv.reader(file)
            header = next(reader)  # Skip the header
            for row in reader:
                data.append(row)

            # separating first and last name and add to modData dictionary
            for row in data:
                last, first = [name.strip() for name in row[0].split(",")]
                house = row[1].strip()
                modData.append({"first": first, "last": last, "house": house})

        # adding modified data from dictionary to csv file
        with open(after, 'w', newline='') as file:
            fields = ['first', 'last', 'house']     # fields name
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(modData)

    # if FileNotFoundError araise then  exit by printing "File does not exist"
    except FileNotFoundError:
        sys.exit("File does not exist")

# Function to check for valid command-line arguments
def valid_file():
    # if number of command-line arguments are less than 3
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    # if number of command line-arguments are greater than 3
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    #storing file names from command line-argument in variable
    before = sys.argv[1]
    after = sys.argv[2]
    # checking files are .csv files
    if before.endswith(".csv") and after.endswith(".csv"):
        return before, after
    # if not a ".csv" file
    else:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
