import cx_Oracle
import sys

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
cursor.execute("SELECT user_id FROM scores")

while True:
	for i in range(1, count+1):
		cursor.execute(f"UPDATE scores SET score = {randint(1,count)} WHERE user_id = {i}")
		
