# Importing modules
import sys
import random
from pyfiglet import Figlet

# Creating object of class figlet()
figlet = Figlet()
# List of all fonts
fList = figlet.getFonts()
# List of command-line arguments
argv= sys.argv
# List of possible symbols use in command-line arguments
fSymbol = ["-f", "--font"]

# Checking for for valid command-line arguments
# If user inputed 3 command-line arguments like python figlet.py -f slant or python figlet.py --font slant
if len(argv) == 3 and argv[2] in fList and argv[1] in fSymbol:
    # Setting font to text which is at index 2 of command-line arguments
    figlet.setFont(font=argv[2])

# If user inputed 1 command-line arguments like python figlet.py.
elif len(argv) == 1:
    # Setting Random font from font list to text which is at index 2 of command-line arguments
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)

# If an invalid command-line arguments entered by user
else:
    # Exiting program which a messages "Invalid usage"
    sys.exit("Invalid usage")

# Taking input from user (text)
text = input("Input: ")
# Printing the text in the new font
print(figlet.renderText(text))
