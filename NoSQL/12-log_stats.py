#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["logs"]
collection = db["nginx"]


lst_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
print("Methods:")
for method in lst_methods:
    count = collection.count_documents({"method": method})
    print("\tmethod {}: {}".format(method, count))

count = collection.count_documents({"method": "GET", "path": "/status"})
print("{} status check".format(count))
