#!/usr/bin/env python3
"""insert new document in a collection"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic
    Args:
        mongo_collection: collection object
        topics ([str]): list with topic names
    Return:
        list of schools
    """
    schools_list = []
    for school in mongo_collection.find({'topics': topic}):
        schools_list.append(school)
    return schools_list
