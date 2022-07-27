#!/usr/bin/env python3
"""This module contains the list_all function
"""


def list_all(mongo_collection):
    """lists all documents in a collection
    """
    if not mongo_collection or not mongo_collection.find():
        return []

    return mongo_collection.find()
