#!/usr/bin/env python3
"""returns all students sorted by average score"""


def top_students(mongo_collection):
    """
    returns all students sorted by average score
    """

    documents = list(mongo_collection.find())
    total = 0
    for document in documents:
        for topic in document["topics"]:
            total += topic["score"]
        average = total / len(document["topics"])

        name = document["name"]
        avg_score = {"averageScore": average}
        mongo_collection.update_many({"name": name}, {"$set": avg_score})

    sorted_scores = mongo_collection.find().sort("averageScore", -1)
    return sorted_scores
