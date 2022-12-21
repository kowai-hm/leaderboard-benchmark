import json
import sqlite3
import sys
import time

from flask import Flask, render_template


app = Flask(__name__)

# Select sample database
if len(sys.argv) > 1:
	db = f"sampledb_{sys.argv[1]}.db"
else:
	db = "sampledb.db"


# SQLite
connection = sqlite3.connect(f"/home/hm/Bureau/leaderboard/sqlite/{db}", check_same_thread=False)
cursor = connection.cursor()


@app.route("/")
def home():
	return render_template("leaderboard.html")
	
@app.route("/scores")
def scores():
	start = time.time()
	cursor.execute("SELECT * FROM scores ORDER BY score DESC")
	end = time.time()
	print(end-start)
	return json.dumps(cursor.fetchall())
	
			
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000)
