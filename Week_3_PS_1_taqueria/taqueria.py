# Total Cost
total = 0
# Memu of Felipe’s Taqueria
menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
}

# Looping to place order
while True:
    try:
        # Prompting them for items
        item = input("Item: ").title()
        if item in menu:
            # Calculating Total Cost
            total += menu[item]
            # Prefixed with a dollar sign ($) and formatted to two decimal places
            f_total = "${:.2f}".format(total)
             # Display the total cost of all items
            print("Total:", f_total)

    # Exit when EOFERROR raise
    except EOFError:
            exit()
