import json
import tarantool

from tarantool.const import ITERATOR_LT
from flask import Flask, render_template


app = Flask(__name__)


# TARANTOOL
connection = tarantool.connect("localhost", 3301, user="admin", password="pass")
scores_space = connection.space("scores")


@app.route("/")
def home():
	return render_template("leaderboard.html")
	
@app.route("/scores")
def scores():
	return json.dumps(list(scores_space.select(index="secondary", iterator=ITERATOR_LT)))
	
			
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000)
