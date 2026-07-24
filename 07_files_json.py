import json

match_data = {
    "home":"osfp",
    "away":"Paok",
    "odds":{"home_win": 1.85, "draw": 3.40, "away_win": 4.20}
}


with open("match.json","w") as f:
    json.dump(match_data, f, indent=4)

with open("match.json","r") as f:
    loaded_data=json.load(f)

print(loaded_data)
print(loaded_data["odds"]["home_win"])