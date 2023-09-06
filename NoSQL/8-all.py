#!/usr/bin/env python3
"""show all documents"""
import pymongo


def list_all(mongo_collection):
    """
    Lists all documents in a collection
    Args:
        mongo_collection: collection object
    Return:
        List with all documents
    """
    documents = []
    for docs in mongo_collection.find():
        documents.append(docs)
    return documents
