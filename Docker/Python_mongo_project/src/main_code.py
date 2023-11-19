import pymongo

myclient = pymongo.MongoClient("mongodb://admin:password@mongodb:27017/")

dblist = myclient.list_database_names()
if "Student" in dblist:
  print("The database exists.")
  mydb = myclient["Student"]
  mycol = mydb["details"]
  mydict = { "name": "John", "address": "Highway 37" ,"city":"dehradun"}
  x = mycol.insert_one(mydict)
else:
    print("hello")
    mydb = myclient["Student"]
    mycol = mydb["details"]
    mydict = { "name": "John", "address": "Highway 37" }
    x = mycol.insert_one(mydict)
myclient.close()