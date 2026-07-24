def divide(a,b):
    try:
        result=a/b
        return result
    except ZeroDivisionError:
        print("den mporeis na diaireseis me to miden")
        return None
    
print(divide(10, 2))
print(divide(10, 0))

def get_odds_value(odds_str):
    try:
        return float(odds_str)
    except ValueError:
        print("mi egkuri timi odds:" , odds_str)
        return None
    
print(get_odds_value("2.5"))
print(get_odds_value("abc"))
