# from pymongo import MongoClient 
# # to create the mongo client connnection

# client = MongoClient("mongodb://localhost:27017")
# #  to create the database using client
# eventdb = client["eventdb"]
# # to create the collections  using database

# addevent = eventdb["addevent"]
# #  to insert the event using coleections

# addevent.insert_one({
#     "eventname":"invertia",
#     "venue":"bareilly",
#     "date":"20 feb 2026"
#     }) 


from pymongo import MongoClient 
# to create the mongo client connnection

client = MongoClient("mongodb://localhost:27017")
#  to create the database using client
eventdb = client["eventdb"]
# to create the collections  using database

addevent = eventdb["addevent"]
#  to insert the event using coleections

# addevent.insert_many([{
#     "eventname":"tedx",
#     "venue":"bareilly",
#     "date":"21 feb 2026"
#     },
#                       {
#     "eventname":"dbatraining",
#     "venue":"bareilly",
#     "date":"2 feb 2026"
#     }]) 



# to delete the dabase from database
addevent.delete_one({
    "eventname":"tedx"
})

