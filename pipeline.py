import psycopg2
import requests
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY =os.getenv("ODDS_API_KEY")
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


# 1. Ορισμός των στοιχείων σύνδεσης
connection_config = {
    "dbname": "sportsbook",
    "user": "postgres",
    "password": os.getenv("DB_PASSWORD"),
    "host": "localhost",       # ή την IP του server σου
    "port": "5432"             # το default port της PostgreSQL
}
for fixture in data:
    home = fixture["home_team"]
    away = fixture["away_team"]
    match_time = fixture["commence_time"]

    try:
    # 2. Δημιουργία σύνδεσης με τη βάση
        with psycopg2.connect(**connection_config) as conn:
        
        # 3. Δημιουργία κέρσορα για την εκτέλεση queries
            with conn.cursor() as cursor:
            
            # 1. Ελέγχουμε στον πίνακα fixtures αν υπάρχει ήδη αυτό το ζευγάρι
                query_check = """
                SELECT id FROM fixtures 
                WHERE home_team = %s AND away_team = %s AND commence_time = %s;
            """
                cursor.execute(query_check, (home, away, match_time))
                result = cursor.fetchone()
            
            # 2. Αν το result είναι None, ο αγώνας ΔΕΝ υπάρχει, οπότε κάνουμε INSERT
                if result is None:
                    query_insert = """
                    INSERT INTO fixtures (home_team, away_team, commence_time) 
                    VALUES (%s, %s, %s)
                    RETURNING id;
            """
                    cursor.execute(query_insert, (home, away, match_time))
                    new_id=cursor.fetchone()[0]
                    print(f"Ο αγώνας {home} vs {away} καταχωρήθηκε επιτυχώς!")
                
                else:
            # Αν βρεθεί, το result[0] περιέχει το υπάρχον id του αγώνα
                    existing_id = result[0]
                    print(f"Ο αγώνας υπάρχει ήδη στα fixtures με ID: {existing_id}")
            
            
                fixture_id = new_id if result is None else existing_id



                for bookmaker in fixture["bookmakers"]:
                    name = bookmaker["title"]
                    for market in bookmaker["markets"]:
                        for outcome in market["outcomes"]:
                            query_insert_odds = """
                            INSERT INTO odds (fixture_id, bookmaker, outcome, price) 
                            VALUES (%s, %s, %s, %s)"""
                            cursor.execute(query_insert_odds,(fixture_id, bookmaker["title"], outcome["name"] ,outcome["price"]))
                conn.commit()   
                         
    except psycopg2.DatabaseError as error:
        print(f"Σφάλμα κατά τη σύνδεση ή την εκτέλεση: {error}")