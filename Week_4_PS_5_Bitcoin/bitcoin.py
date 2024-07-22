import sys
import requests

# checking for 2 Command-line argument
if len(sys.argv) == 2:
    #trying to get a float input
    try:
        coin = float(sys.argv[1])

    # printing message and exit for any other value then number
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

else:
    print("Missing command-line argument")
    sys.exit(1)

# getting the current price of bitcoin in usd
try:
    # reuesting for the json object
    respone = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    # Extracting the price of bitcoin from json object
    price = respone.json()["bpi"]["USD"]["rate_float"]
    # Calculating the total value of coins inputed from user
    total = round(coin*price, 4)
    print(f"${total:,.4f}")

# Print "RequestException" if requests.RequestException raise and exit the program
except requests.RequestException:
    print("RequestException")
    sys.exit(1)
