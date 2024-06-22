# Data, items and their number of calories 
nutrition = {
                "apple": "130",
                "avocado": "50",
                "banana": "110",
                "Cantaloupe": "50",
                "grapefruit": "60",
                "grapes": "90",
                "Honeydew Melon": "50",
                "kiwifruit": "90",
                "lemon": "15",
                "lime": "20",
                "nectarine": "60",
                "orange": "60",
                "peach": "60",
                "pear": "100",
                "pineapple": "50",
                "plums": "70",
                "strawberries": "50",
                "sweet cherries": "100",
                "tangerine": "50",
                "watermelon": "80"
}

# Prompts users to input a fruit (case-insensitively)
item = input("Item: ").lower()

# Checking either the fruit is in data or not 
# If fruit is in data, printing the calories it contain
if item in nutrition:
    print("Calories:", nutrition[item])

# If fruit is not in data     
else:
     print("")
