#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")
    db = client["logs"]
    collection = db["nginx"]

    lst_method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    dic_method_count = {}
    # create a dictionary with method and the count of methods
    for method in lst_method:
        dic_method_count[method] = collection.count_documents({"method": method})

    # Count the number of documents with method=GET and path=/status
    status_count = collection.count_documents({"method": "GET", "path": "/status"})

    # Show method counts
    print("Methods:")
    for k, v in dic_method_count.items():
        print(f"\tmethod {k}: {v}")

    print(f"{status_count} status check")

