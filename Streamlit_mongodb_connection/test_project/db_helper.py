from pymongo import MongoClient
from bson import ObjectId
import streamlit as st


client = MongoClient("mongodb://localhost:27017") 
db = client["abi"]       
collection = db["abi"]


def insert_data(data):
    collection.insert_one(data)

def get_all_data():
    return list(collection.find())

def update_data_by_name(name, new_data):
    collection.update_one({"name": name}, {"$set": new_data})

def delete_data_by_name(name):
    # Check if a document with that name exists
    record = collection.find_one({"name": name})
    
    if record:
        collection.delete_one({"name": name})
        st.success(f"Record for '{name}' deleted ✅")
    else:
        st.warning("⚠️ Enter valid username!")

def search_data_by_name(name):
    return list(collection.find({"name": name}))
