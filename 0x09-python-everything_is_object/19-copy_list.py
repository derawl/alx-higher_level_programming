#!/usr/bin/python3

"""
This module  copies a list
"""


def copy_list(l):
    """Function that returns the copy of a list
    Args:
        l: list
    Returns:
        a new list
    """
    new_list = l[:]
    return new_list
