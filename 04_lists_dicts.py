teams=["osfp","paok","aek"]
print(teams[0])          # πρώτο στοιχείο -> Olympiacos
print(teams[-1])         # τελευταίο στοιχείο -> AEK
teams.append("Aris")     # προσθήκη στο τέλος
print(teams)

for team in teams:
    print(team)

match={
    "home":"osfp",
    "away":"paok",
    "score_home":2,
    "score_away":1
}

print(match["home"])           # -> Olympiacos
print(match["score_home"]) 

match["status"]="finished"
print(match)

for key,value in match.items():
    print(key, "->",value)