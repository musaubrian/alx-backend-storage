#!/usr/bin/env python3
""" lists all documents in a collection"""
import pymongo


def list_all(mongo_collection):
    """
    returns a list of documents in a collection
    empty list if no documents in the collection
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
