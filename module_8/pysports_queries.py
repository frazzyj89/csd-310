#JOshua Frazier
#july 3, 2022
#module 8.3 pysport queries

import mysql.connector

#connect to the db
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password="5133Frazi3r!",
    database="pysports"
)

#create cursor
cursor = db.cursor()

#Query
query_1 = "SELECT team_id, team_name, mascot FROM team"
query_2 = "SELECT player_id, first_name, last_name, team_id FROM player"

#execute
cursor.execute(query_1)
cursor.execute(query_2)

for team in cursor:
    print(team)
for player in cursor:
    print(player)
    
cursor.close()

db.close()
