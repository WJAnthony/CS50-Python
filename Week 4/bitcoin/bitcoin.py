import requests
import sys
import requests
import json

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    o = response.json()
    price = float(o["bpi"]["USD"]["rate_float"])
    amount = price * float(sys.argv[1])
    print(f"${amount:,.4f}")

except requests.RequestException:
    sys.exit("Command-line arguement is not a number")

except ValueError:
    sys.exit("Command-line arguement is not a number")
