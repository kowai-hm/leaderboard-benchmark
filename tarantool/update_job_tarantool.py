import tarantool

from random import randint


# TARANTOOL
connection = tarantool.connect("localhost", 3301, user="admin", password="pass")
scores_space = connection.space("scores")
users = [user for user, score in scores_space.select()]


while True:
	for user in users:
		scores_space.update(user, [("=", "score", randint(1,20))])
