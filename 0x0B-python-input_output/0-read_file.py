#!/usr/bin/python3
"""
This module reads a file name
"""


def read_file(filename=""):
    """Prints the contents of a file
    Arguments:
     filename: name of the file
    """
    with open(filename) as file:
        print(file.read())
