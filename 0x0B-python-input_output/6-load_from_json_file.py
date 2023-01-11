#!/usr/bin/python3
""" Module creates an Object(python ds) from a JSON file
"""
import json


def load_from_json_file(filename):
    """ Function creates an Object from a JSON file
    Args:
        filename: file name
    Raises:
        Exception: when the object can't be encoded
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
