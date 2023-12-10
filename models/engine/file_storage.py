#!/usr/bin/python3
"""
This modules help provide a convenient storage format via
functions that will help in the serialisation to json and also
the deserialsation from json format
"""
import json
import os
import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Class that helps in the management and loading of
    data - serialization and deserialisation for storage and usage
    REpresents an abstracted storage engine
    Attributes:
        __file_path (str): path to JSON file
        __objects (dict): empty but will store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj_class_name>.id"""
        object_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(object_class_name, obj.id)] = obj
    
    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}

        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. 
        If the file does not exist, no exception should be raised)"""
        try:
            with open(FileStorage.__file_path) as file:
                object_dict = json.load(file)
                for objt in object_dict.values():
                    class_name = objt["__class__"]
                    del objt["__class__"]
                    self.new(eval(class_name)(**objt))
        except FileNotFoundError:
            return




