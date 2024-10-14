#!/usr/bin/python3
"""Serializing and Deserializing with XML"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    It should serialize the dictionary into XML
    and save it to the given filename.
    """
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Read the XML data from that file,
    and return a deserialized Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary