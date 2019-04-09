
# let's grab the data from a public API and parse the data

# let's use the urllib library to get information from a yahoo API
import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()
# print all the contents of the website
print(source)

# let's convert this into a python object
data = json.loads(source)

# Let's print this json file
print(json.dumps(data, indent=2))

usd_rates = dict()

for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price

print(50 * float(usd_rates['USD/INR']))