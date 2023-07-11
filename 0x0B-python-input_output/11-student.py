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

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance


        Args:
            attrs (list, optional): list of strings. Defaults to None.

        Returns:
            dict: dictionary representation
        """
        if not isinstance(attrs, list):
            return self.__dict__

        if not all(isinstance(element, str) for element in attrs):
            return self.__dict__

        my_dict = {}
        for key in attrs:
            if key in self.__dict__:
                my_dict[key] = self.__dict__[key]
        return my_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance

        Args:
            json (json string): dictionary json
        """
        for key, value in json.items():
            setattr(self, key, value)
