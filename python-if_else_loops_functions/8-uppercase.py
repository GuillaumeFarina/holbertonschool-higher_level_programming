#!/usr/bin/python3

def uppercase(str):
    uppercase = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase += chr(ord(char) - 32)
        else:
            uppercase += char
    print("{}".format(uppercase))
