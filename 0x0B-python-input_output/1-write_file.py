#!/usr/bin/python3
"""Module writes to a file"""


def write_file(filename="", text=""):
    """Function returns the number of characters written to a file
    Args:
     filename: filename
     text: text 
    Returns:
        number of chracters written
        
    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_xters = file.write(text)
        return num_xters
