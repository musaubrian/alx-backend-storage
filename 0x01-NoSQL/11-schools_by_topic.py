#!/usr/bin/env python3
"""returns the list of school having a specific topic"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school with a specific topic
    """
    mongo_collection = mongo_collection.find({"topics": topic})
    return mongo_collection
