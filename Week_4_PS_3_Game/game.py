import random

# num variable store a random number in range of 1 to 101 
num = random.choice(range(1, 101))

# looping untill user enter a valid input for level
while True:
    try:
        # Prompts the user for a level
        level = int(input("Level: "))
        # Checking for valid positive integer for level 
        # If the user does not input a positive integer, the program should prompt again.
        if level>0:
            break
        else:
            continue
        
    # loop will continue and ask again, if input is other than a integer  
    except ValueError:
        pass

# looping untill user enter a valid input for guess
while True:
    try:
        # Prompts the user for a guess
        inptNum = int(input("Guess: "))
         # Checking for valid positive integer for guess
        # If the user does not input a positive integer, the program should prompt again.
        if inptNum>0:
            # If inputted integer is equal to random number store in num variable, it print "Just right!" message and break loop 
            if inptNum == num:
                print("Just right!")
                break
            # If inputted integer is greater than random number store in num variable, it print "Too large!" message and continue loop and ask again for guess number 
            elif inptNum>num:
                print("Too large!")
                continue
            # If inputted integer is less than random number store in num variable, it print "Too small!" message and continue loop and ask again for guess number 
            elif inptNum<num:
                print("Too small!")
                continue
        else:
            continue

    # loop will continue and ask again, if input is other than a integer  
    except ValueError:
        pass
    