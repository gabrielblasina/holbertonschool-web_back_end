#!/usr/bin/env python3
"""insert new document in a collection"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Lists all documents in a collection
    Args:
        mongo_collection: collection object
        **kwargs: key-value pairs of the fields to be inserted
    Return:
        the new _id
    """
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
