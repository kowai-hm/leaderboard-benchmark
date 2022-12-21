import sqlite3
import statistics
import sys
import time

from random import randint


# Select sample database
if len(sys.argv) > 1:
	db = f"sampledb_{sys.argv[1]}.db"
	count = int(sys.argv[1])
else:
	db = "sampledb.db"
	count = 1000000


# SQLite
connection = sqlite3.connect(f"/home/hm/Bureau/leaderboard/sqlite/{db}", isolation_level=None)
cursor = connection.cursor()


execution_times = []
while True:
	start = time.time()
	for i in range(1, count+1):
		cursor.execute(f"UPDATE scores SET score = {randint(1,count)} WHERE user_id = {i}")
	end = time.time()
	execution_times.append(end-start)
	print(end-start)
	if len(execution_times) == 11:
		print(f"Average execution time for 10 tries : {statistics.mean(execution_times[1:])}")
		
