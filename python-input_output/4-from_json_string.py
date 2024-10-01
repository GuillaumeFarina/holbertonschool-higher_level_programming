#!/usr/bin/python3
"""
This module contains a function that returns an object
(Python data structure) represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Arguments:
    my_str -- the JSON string to convert

    Returns:
    The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
