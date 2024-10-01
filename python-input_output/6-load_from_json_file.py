#!/usr/bin/python3
"""Load From a JSON file"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
