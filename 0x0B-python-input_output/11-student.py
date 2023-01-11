#!/usr/bin/python3
""" Module defines the class Student
"""


class Student:
    """ Class create instances of students """

    def __init__(self, first_name, last_name, age):
        """ Special method to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method that returns directory description """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            dict_list = {}

            for iatr in range(len(attrs)):
                for jatr in obj:
                    if attrs[iatr] == jatr:
                        dict_list[jatr] = obj[jatr]
            return dict_list

        return obj

    def reload_from_json(self, json):
        """ Replace all attributes of the Student instance """
        for atr in json:
            self.__dict__[atr] = json[atr]
