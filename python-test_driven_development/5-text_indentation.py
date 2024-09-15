#!/usr/bin/python3
"""
 prints a text with 2 new lines after each of specific char.
"""


def text_indentation(text):
    """
    prints a test
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    if text:
        for char in ".?:":
            text = text.replace(char, char + "\n\n")
        text = "\n".join([line.strip() for line in text.split("\n")])
        print(text.strip(), end="")
