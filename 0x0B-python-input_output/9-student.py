#!/usr/bin/python3

""" defines a class student."""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """special method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method return"""
        return self.__dict__
