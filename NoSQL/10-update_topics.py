#!/usr/bin/env python3
"""insert new document in a collection"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    change all topics of a school document based on the name
    Args:
        mongo_collection: collection object
        name (str) : name of the school to be updated
        topics ([str]): list with topic names
    Return:
        void
    """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
