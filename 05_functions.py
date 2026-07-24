def greet(name):
    print("geia sou, ",name)

greet("Marina")
greet("Thanos")

def add(a,b):
    result=a+b
    return result
total=add(5,3)
print(total)

def calculate_odds_profit(stake, odds=2.0):
    return stake*odds

print(calculate_odds_profit(10))
print(calculate_odds_profit(10,3.5))