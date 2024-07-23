def main():
    # Taking input(Greeating)
    greeting = input("Greeting: ")
    # Printing value of greeting
    print("$", value(greeting), sep = "")

# Function to return value of greeting
def value(greeting):
    greet = greeting.lower()
    # Checking if "Hello" is in the input or not and return 0
    if "hello" in greet:
        return 0
    # Checking input start with "h" and return 20
    elif greet.startswith("h"):
        return 20
    # else return 100
    else:
        return 100

if __name__ == "__main__":
    main()

