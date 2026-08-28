import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

# 1. Ορισμός των στοιχείων σύνδεσης
connection_config = {
    "dbname": "sportsbook",
    "user": "postgres",
    "password": os.getenv("DB_PASSWORD"),
    "host": "localhost",       # ή την IP του server σου
    "port": "5432"             # το default port της PostgreSQL
}



try:
    # 2. Δημιουργία σύνδεσης με τη βάση
    with psycopg2.connect(**connection_config) as conn:
        
        # 3. Δημιουργία κέρσορα για την εκτέλεση queries
        with conn.cursor() as cursor:
            
            # 1. Βάζεις το δικό σου query
            query = """SELECT home_team,away_team,price,created_at FROM odds
                     JOIN fixtures ON fixtures.id=odds.fixture_id
                     WHERE fixtures.home_team = 'Arsenal' AND fixtures.away_team = 'Coventry City'
                     AND odds.bookmaker='Pinnacle' AND odds.outcome='Arsenal'
                     ORDER BY created_at;"""
            cursor.execute(query)
            
            # 2. Παίρνεις όλες τις γραμμές μαζί
            rows = cursor.fetchall()
            
            # 3. Κάνεις loop για να τις τυπώσεις
            for row in rows:
                print(row)  # Κάθε 'row' είναι ένα tuple (π.χ. (1, 'Γιώργος', 1500))

except psycopg2.DatabaseError as error:
    print(f"Σφάλμα κατά τη σύνδεση ή την εκτέλεση: {error}")
