#!/usr/bin/python3
"""
FileStorage module
"""
from json import dump, load
from os import path
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review


class FileStorage:
    """
    the storage class to store an instance of any model
    """
    __file_path = "file.json"
    __objects = {}
    
    def all(self, cls=None):
        """
        Returns a dictionary of every object stored.
        If cls is specified, only objects of that class are returned.
        """
        if cls is None:
            # If no class is specified, return the entire objects dictionary.
            return self.__objects
        else:
            # If a class is specified, create a new dictionary to hold objects of that class.
            class_name = cls.__name__
            objects_of_class = {}
            # Loop through every key-value pair in the objects dictionary.
            for key, value in self.__objects.items():
                # Check if the value's class name matches the specified class name.
                if class_name == value.__class__.__name__:
                    # If it does, add the key-value pair to the new dictionary.
                    objects_of_class[key] = value
                    # Return the new dictionary containing objects of the specified class.
                    return objects_of_class
    
    def new(self, obj):
        """
        The new(obj) method adds a new object to the __objects dictionary.
        """
        self.__objects[obj.__class__.__name__ + '.' + str(obj.id)] = obj
    
    def save(self):
        """
        Serializes __objects to the JSON file __file_path
        """
        new_dict = {}
        for key, value in self.__objects.items():
             new_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            dump(new_dict, file)
    
    def reload(self):
        """
        Deserializes the JSON file __file_path to __objects
        """
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                obj_dict = load(file)
            for key, value in obj_dict.items():
                class_name = value["__class__"]
                self.__objects[key] = eval(class_name + "(**value)")
        except FileNotFoundError:
            pass
