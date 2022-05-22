import requests
from data import my_api_currency
from datetime import date

today = date.today()

API_KEY = my_api_currency
DATE = today
CURRENCIES_LIST = "EUR,PLN,CHF"
my_url = f"https://api.apilayer.com/currency_data/historical?&date={DATE}&currencies={CURRENCIES_LIST}"
my_headers = {'apikey': API_KEY}


response = requests.get(my_url, headers=my_headers)
response_json = response.json()
print(response_json)

usd_per_pln = response_json["quotes"]["USDPLN"]
usd_per_eur = response_json["quotes"]["USDEUR"]
usd_per_frank = response_json["quotes"]["USDCHF"]

print("USD per PLN: " + str(usd_per_pln))
print("USD per EUR: " + str(usd_per_eur))
print("USD per CHF: " + str(usd_per_frank))
