# Empty dictionary for grocery which contain the items and the number of time that item enter by user
grocList = {}

# Looping to get items from user
while True:
    try:
        # prompting user to enter item
        item = input().upper()

        # If the inputted item not exist in the grocery dictionary, asign the value to that item 1
        if not item in grocList:
            grocList[item] = 1
        # If the inputted item exist in the grocery dictionary, increased the value to that item by 1
        else:
            grocList[item] += 1

    # Exit when EOFERROR raise
    except EOFError:
        # Sorting the grocery dictionary
        itemsList = list(grocList.keys())
        itemsList.sort()
        sorted_grocList = {i: grocList[i] for i in itemsList}

        # Printing the items of grocery dictionary and the number of time it entered
        for item in sorted_grocList:
            print(sorted_grocList[item], item)

        # Exit wwhen user enter control-d/control-z
        exit()
