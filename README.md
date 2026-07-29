# Live Odds Pipeline

## What it does
Takes live odds from various bookmakers via API and stores them in PostgreSQL, allowing comparison with past odds over time (line movement tracking).

## Tech stack
Python, PostgreSQL, psycopg2, requests, python-dotenv

## How to run it
1. Clone the repo: git clone https://github.com/maroik19/sportsbook-odds-pipeline.git
2. Install dependencies: pip install -r requirements.txt
3. Create a `.env` file in the project root with: 
   ODDS_API_KEY=your_api_key_here
   DB_PASSWORD=your_db_password_here
4. Make sure PostgreSQL is running locally with a database named `sportsbook`, and the `fixtures`/`odds` tables created.
5. Run the script: `python pipeline.py`