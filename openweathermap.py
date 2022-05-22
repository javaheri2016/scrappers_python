import requests
from data import my_api_weather

API_KEY = my_api_weather

longitudes = [20, 21]
latitudes = [51, 52]
cities = ["Kraków", "Warszawa"]
pm10s = []

for i, j, k in zip(longitudes, latitudes, cities):
    my_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={i}&lon={j}&appid={API_KEY}"
    response = requests.get(my_url)
    response_json = response.json()
    pm10s.append(response_json["list"][0]["components"]["pm10"])

print(pm10s)

i = 0
for m, n in zip(cities, pm10s):
    print("wyniki: " + str(cities[i]) + " " + str(pm10s[i]))
    i = i + 1



