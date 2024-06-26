# Importing inflect module
import inflect

# Creating object "p" for inflect.engine()
p = inflect.engine()
# List to store names enter by user
names = []

# Looping untill user enter "controll-d" or "controll-z"
while True:
    try:
        # Promoting user to enter name
        name = input("Name: ")
        # Add that name to list "names"
        names.append(name)
    except EOFError:
        # Break the loop when user enter "controll-d" or "controll-z"
        break

# Print the statement along with the names using join function of inflect module
print("Adieu, adieu, to", p.join(names))
