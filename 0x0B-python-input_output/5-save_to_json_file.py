#!/usr/bin/python3
""" Module contains a function that returns an object from
a JSON string representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ Function that saves a json object to a file
    Args:
        my_obj: JSON object
    Raises:
        Exception: when the string can't be decoded
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
