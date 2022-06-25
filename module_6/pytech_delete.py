#import MongoClient
from pymongo import MongoClient

#create a variable named url
url = "mongodb+srv://admin:admin@cluster0.zw2hy57.mongodb.net/?retryWrites=true&w=majority"

#create a variable named client
client = MongoClient(url)

#create a variable named db
db = client.pytech
#defining students and docs to efficiently search with find() function
students = db.students
docs = db.students.find({})
print("\n DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in docs:
    print("Students ID:" + doc["student_id"] + "\n First Name:" + doc["first_name"] + "\n Last Name:" + doc["last_name"] + "\n")

db.students.update_one({"student_id":"1007"}, {"$set":{"last_name":"Thunderbolt"}})

Frazier=students.find_one({"student_id":"1007"})

print("Student ID:"+Frazier["student_id"]+"\n First Name:"+Frazier["first_name"]+"\nLast Name:"+Frazier["last_name"]+"\n")
#eop
input("\n\n End of Program, press any key to exit...")



