#!/usr/bin/env python3
"""Insert a document in Python and Returns the new inserted_id"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document into mongodb collection based on kwargs"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
