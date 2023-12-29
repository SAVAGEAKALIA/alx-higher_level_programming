#!/usr/bin/python3
""" Project for *arg and **kwarg """
from json import dumps, loads


class Base:
    """
    bass class created for function
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base object.

        Args:
            id (int): The ID of the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def get_object_count(cls):
        """
        Get the count of created objects.

        Returns:
            int: The count of created objects.
        """
        return cls.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return JSON string for if list_dictionaries is
        not None

        @param list_dictionaries:
        @return: JSON String format
        """
        if list_dictionaries is None or list_dictionaries == "":
            return "[]"
        return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string
        representation json_string

        @param json_string:
        @return: dictionary representation python
        """
        if json_string is None or json_string == "":
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs
        to a file
        @param list_objs: is a list of instances who
        inherits of Base
        example: list of Rectangle or list of Square instances
        @return: file
        """

        filename = cls.__name__ + ".json"

        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is not None:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                json_file = cls.to_json_string(list_dicts)
                for arg in json_file:
                    f.write(arg)
            else:
                f.write("[]")

    @classmethod
    def create(cls, **dictionary):
        """
        Create a dummy method
        that returns an instance with all attributes already set
        @param dictionary:
        @return:
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Class method that returns a list of instances
        @return:
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                json_str = f.read()
                list_dicts = cls.from_json_string(json_str)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
