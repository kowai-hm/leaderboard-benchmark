import cx_Oracle
import statistics
import sys
import time

from random import randint


# Select sample database
if len(sys.argv) > 1:
	dsn = f"sampledb_{sys.argv[1]}"
	count = int(sys.argv[1])
else:
	dsn = "sampledb"
	count = 1000000


# TIMESTEN
connection = cx_Oracle.connect(dsn=dsn)
connection.autocommit = True
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
		
