from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["abi"]
collection = db["abi"]


def insert_data(Data):
    collection.insert_one(Data)
