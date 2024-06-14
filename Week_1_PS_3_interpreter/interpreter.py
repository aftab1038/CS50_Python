# Taking input (mathematical expression)
expression = input("Expression: ")

# Separating numbers and operator
# x is 1st number,  y is operator,  z ia 2nd number
x, y, z = expression.split(" ")

# Converting string numbers to floating numbers
x = float(x)
z = float(z)

# Calculating the answer based on the operator inputted
match y:
    case "+":
        print(x+z)
    case "-":
        print(x-z)
    case "*":
        print(x*z)
    case "/":
        print(x/z)
    case _:
        print("Invalid Input")

