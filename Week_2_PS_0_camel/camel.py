# Taking input {camelCase}
inpt = input("camelCase: ")

# looping through each character
for c in inpt:
    # Finding the character(s) in Upper Case
    if c.isupper():
       # Change the upper Case character(s) with "_*"
       inpt = inpt.replace(c, "_*")
       # Change the * with the lower case of character(s) which was in upper case previously
       inpt = inpt.replace("*", c.lower())

# Print the output {snake_case}
print("snake_case:", inpt)
