from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.dbsparta

mycol = db["movies"]

mycol.drop()