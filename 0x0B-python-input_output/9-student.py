#!/usr/bin/python3
"""class Student"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Instantiate the student instance

        Args:
            first_name (str): the first name of the student
            last_name (str):the last name of the student
            age (int): the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance

        Returns:
            dict: dictionary representation
        """
        return self.__dict__
