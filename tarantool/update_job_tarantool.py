import statistics
import tarantool
import time

from random import randint


# TARANTOOL
connection = tarantool.connect("localhost", 3301, user="admin", password="pass")
scores_space = connection.space("scores")
users = [user for user, score in scores_space.select()]


execution_times = []
while True:
	start = time.time()
	for user in users:
		scores_space.update(user, [("=", "score", randint(1,len(users)))])
	end = time.time()
	execution_times.append(end-start)
	print(end-start)
	if len(execution_times) == 11:
		print(f"Average execution time for 10 tries : {statistics.mean(execution_times[1:])}")
