#JOshua Frazier
#july 10, 2022
#module 9.2 pysport join_queries

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "5133Frazi3r!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)
# Query
query_1 = "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id"
# create cursor
cursor = db.cursor()
# execute
cursor.execute(query_1)
players = cursor.fetchall()
print("\n -- DISPLAYING PLAYER RECORDS -- ")
for player in players:
    print("\n Player ID: {} \n First Name: {} \n Last Name: {} \n Team ID: {}".format(player[0], player[1], player[2], player[3]))

input ("\n\n Press any key to continue...")