# Taking input from user
inpt = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
inpt = inpt.lower().strip()

# Matching the input
match inpt:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
