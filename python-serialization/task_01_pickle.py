#!/usr/bin/env python3
"""Pickling Custom Classes"""
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """
        Initialize with name, age, and student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Displays the attributes of the object.
        """
        print("Name: {}\nAge: {}\nIs Student: {}\n"
              .format(self.name, self.age, self.is_student))

    def serialize(self, filename):
        """
        Serializes the object(binary) and saves it to a file using pickle.
        """
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes the object(binary).
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None
