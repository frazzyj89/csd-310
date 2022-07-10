#JOshua Frazier
#july 10, 2022
#module 9.3 pysport updates and deletes


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

cursor = db.cursor()

sql = "INSERT INTO player (first_name, last_name, team_id) VALUES (%s,%s,%s)"
cursor.execute(sql, ('Smeagol', 'Shire Folk', 1))

sql = "UPDATE player SET team_id=2, first_name='Gollum', last_name='Ring Stealer' WHERE first_name='Smeagol'"
cursor.execute(sql)

sql = "DELETE FROM player WHERE first_name = 'Gollum'"
cursor.execute(sql)

sql = "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id"
cursor.execute(sql)


players = cursor.fetchall()
print("\n -- DISPLAYING PLAYER RECORDS -- ")
for player in players:
    print("\n Player ID: {} \n First Name: {} \n Last Name: {} \n Team Name: {}".format(player[0], player[1], player[2],
                                                                                        player[3]))

input ("\n\n Press any key to continue...")
