import cx_Oracle
import sys

from random import randint


# Select sample database
if len(sys.argv) > 1:
	dsn = f"sampledb_{sys.argv[1]}"
	nb = int(sys.argv[1])
else:
	dsn = "sampledb"
	nb = 1000000


connection = cx_Oracle.connect(dsn=dsn)
connection.autocommit = True
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
