#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    text = text.strip()
    if text:
        for char in ".?:":
            text = text.replace(char, char + "\n\n")
        print(text)
