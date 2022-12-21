import json
import tarantool
import time

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
	start = time.time()
	s = scores_space.select(index="secondary", iterator=ITERATOR_LT)
	end = time.time()
	print(end-start)
	return json.dumps(list(s))
	
			
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000)
