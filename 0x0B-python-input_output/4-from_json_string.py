#!/usr/bin/python3
""" Module contains a function that returns an object from
a JSON string representation
"""
import json


def from_json_string(my_str):
    """ Function that returns an object from aJSON representation
    Args:
        my_str: JSON string of the object
    Raises:
        Exception: when the string can't be decoded
    """
    return json.loads(my_str)
