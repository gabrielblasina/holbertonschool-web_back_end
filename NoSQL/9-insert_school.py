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
    data = {'school_data': kwargs}
    new_data = mongo_collection.insertOne(data)
    return new_data.inserted_id
