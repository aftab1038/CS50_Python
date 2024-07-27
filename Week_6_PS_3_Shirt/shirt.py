import sys
from os.path import splitext
from PIL import Image, ImageOps


def main():
    # Checking valid files enter by user
    validFiles()

    # Opening before image
    try :
        before = Image.open(sys.argv[1])

    except FileNotFoundError:
        sys.exit("Input does not exist")

    # Opening the shirt image
    shirt  = Image.open("shirt.png")
    # size of shirt
    size = shirt.size

    # fitting the shirt to before file
    after = ImageOps.fit(before, size)

    # overlapping
    after.paste(shirt, shirt)

    # outputing the after file
    after.save(sys.argv[2])

# Checking Valid files are input or not
def validFiles():
    # Checking command line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    before = sys.argv[1]                # Input file
    before = splitext(before)      # Separating output file name and extension
    after = sys.argv[2]                 # Output file
    after = splitext(after)        # Separating output file name and extension

    # Checking for valid Extension of files
    if not before[1].lower() in  [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid input")
    if not after[1].lower() in  [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid output")

    # Checking both file have same extension
    if before[1].lower() !=  after[1].lower():
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
