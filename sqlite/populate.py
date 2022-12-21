import sqlite3
import sys

from random import randint


# Select sample database
if len(sys.argv) > 1:
	db = f"sampledb_{sys.argv[1]}.db"
	nb = int(sys.argv[1])
else:
	db = "sampledb.db"
	nb = 1000000


connection = sqlite3.connect(db, isolation_level=None)
cursor = connection.cursor()

cursor.execute("""
	CREATE TABLE scores (
		user_id INT PRIMARY KEY NOT NULL,
		score INT NOT NULL
	);
""")

for i in range(1, nb+1):
	print(f"INSERT {i}/{nb}")
	cursor.execute(f"INSERT INTO scores VALUES ({i}, {randint(1,nb)})")

cursor.close()
connection.close()
