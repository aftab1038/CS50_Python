import sys


def main():
    # Getting Valid file name by calling function "valid_pyfile()"
    Fname = valid_pyfile()
    # Trying to open the file if found
    try:
        # openning the file in read mode
        with open(Fname) as file:
            # Getting lines from file and stor in list named as lines
            lines = file.readlines()
            # printing the number of lines of code by calling function LOC_counter()
            print(LOC_counter(lines))
    # if FileNotFoundError araise then  exit by printing "File does not exist"
    except FileNotFoundError:
        sys.exit("File does not exist")

# Function to check for valid command-line arguments
def valid_pyfile():
    # if number of command-line arguments are less than 2
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    # if number of command line-arguments are greater than 2
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    # else if number of command line-arguments are 2
    else:
        # Checking for valid file type, must be ".py" file
        fname = sys.argv[1]
        # if the sencond argument have extension .py the return that
        if fname[-3:] == ".py":
            return fname
        # if not a ".py" file
        else:
            sys.exit("Not a Python file")

# Function to count number of lines of code (LOC), excluding comments and blank lines
def LOC_counter(lines):
    # Looping through each line
    counter = 0             # Counter varible to count the code lines
    for line in lines:
        # if a line is a comments and blank lines,then pass,do nothing
        if line.lstrip().startswith("#") or line.isspace():
            pass
        # else increment the counter by 1
        else:
            counter += 1
    # Return the value of counter (which contain number of code line)
    return counter


if __name__ == "__main__":
    main()
