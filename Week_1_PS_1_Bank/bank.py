# Taking input(Greeating)
greet = input("Greeting: ").lower()

# Checking if "Hello" is in the input or not
if "hello" in greet:
    print("$0")
# Checking input start with "h"
elif greet.startswith("h"):
    print("$20")
else:
    print("$100")
