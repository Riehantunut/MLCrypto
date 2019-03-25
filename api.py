import requests  # pip install requests
import json


# Prints last 100 minutes opening prices of Bitcoin in USD.
lim = 100
r = requests.get('https://min-api.cryptocompare.com/data/histominute?fsym=BTC&tsym=USD&limit=' + str(lim))
toJson = r.text

j = json.loads(toJson)

data = j["Data"]  # This is a list of every unit (in this case minutes) where every unit is a dictionary

for x in range(lim):
    print(data[x]["open"])
