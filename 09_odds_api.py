import requests

API_KEY ="576c4b54e9afe92979d2f3a3bbc0ef6f"
SPORT = "soccer_epl"

url = f"https://api.the-odds-api.com/v4/sports/{SPORT}/odds"
params = {
    "apiKey": API_KEY,
    "regions": "eu",
    "markets": "h2h"
}

response = requests.get(url, params=params)
print(response.status_code)
data = response.json()
#print(data)
print(data[0])  # πρώτο fixture


for bookmaker in data[0]["bookmakers"]:
    name = bookmaker["title"]
    for market in bookmaker["markets"]:
        for outcome in market["outcomes"]:
            print(name, "-", outcome["name"], ":", outcome["price"])