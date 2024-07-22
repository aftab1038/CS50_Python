# Importing Random module
import random

# Main function
def main():
    # Getting level by calling get_level() function
    level = get_level()
    # variables
    question = 10   # Total question
    score = 0       # Counting score
    cout = 0        # Counting number of Question asked

    # Asking 10 questions using loop
    while cout < question:
        cout += 1   # incrementing cout variable value after asking a question
        # Getting random numbers according to inputted level
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        # variable to cout 3 tries if wrong answer is inputed
        tries = 0

        # asking user to inputed answer
        while True:
            # ask untill user inputted a integer
            try:
                tries += 1
                # asking question
                print(num1, "+", num2, "=", end=" ")
                # taking answer from user
                answer = int(input())
                # Checking answer
                if answer == num1+num2:
                    score += 1  # incrementing score if correct
                    break       # breaking loop if correct
                # Printig EEE for wrong answer
                print("EEE")
                # Checking tries, no more than 3 tries
                if tries == 3:
                    # Print answer after 3 tries and breaking loop
                    print(num1, "+", num2, "=", end=" ")
                    print(num1+num2)
                    break
            # If user inputted other value than integer
            except ValueError :
                # Printig EEE for wrong answer
                print("EEE")
                # Checking tries, no more than 3 tries
                if tries == 3:
                     # Print answer after 3 tries and breaking loop
                    print(num1, "+", num2, "=", end=" ")
                    print(num1+num2)
                    break
                pass
    # Last print the score
    print("Score:", score)

# Function to get level from user
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
            else:
                continue
        except ValueError:
            pass

# Function to generate random numbers according to level inputted
def generate_integer(level):
    if level == 1:
        return random.randrange(0, 10)
    if level == 2:
        return random.randrange(10, 100)
    if level == 3:
        return random.randrange(100, 1000)


if __name__ == "__main__":
    main()
