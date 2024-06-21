# Variables
amount = 50     # Amount Due -initially it is price of Coca-Cola (Coke) which is 50 cents
insert = 0      # Coin inputted by user -initially it is zero
total = 0       # total money entered by user -initially it is zero

# taking coins in these denominations only: 25 cents, 10 cents, and 5 cents.
while True:
    # Print the Amount Due
    print("Amount Due:", amount)
    # Taking coin from user and storing it in insert variable
    insert = int(input("Insert Coin: "))

    # Checking the inputted coin, does it is in these denominations only: 25 cents, 10 cents, and 5 cents
    if insert== 25 or insert == 10 or insert == 5:
        # Subtracting inputted coin from amount to get new due amount(amount remaining)
        amount -= insert
        # calculating the total money inputted by user
        total += insert

        # Stop the loop when entered money is greater than or equal to price of coke, 50 cents
        # Finding the change
        if amount <= 0:

            print("Change Owed:", total - 50 )
            break

    # If coin is not in these denominations only: 25 cents, 10 cents, and 5 cents, asking again
    else:
        continue

