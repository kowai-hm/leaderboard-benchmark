import json
import cx_Oracle
import sys

from flask import Flask, render_template


app = Flask(__name__)

# Select sample database
if len(sys.argv) > 1:
	dsn = f"sampledb_{sys.argv[1]}"
else:
	dsn = "sampledb"


# TIMESTEN
connection = cx_Oracle.connect(dsn=dsn)
connection.autocommit = True
cursor = connection.cursor()


@app.route("/")
def home():
	return render_template("leaderboard.html")
	
@app.route("/scores")
def scores():
	cursor.execute("SELECT * FROM scores ORDER BY score DESC")
	return json.dumps(cursor.fetchall())
	
			
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000)
