#!/usr/bin/python3
"""This whole module has the sole purpose to define
       the base model for our modules/classes"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Represents the parent class from which all subsequent classes
    will inherit from. Its the base model of the project"""
    def __init__(self, *args, **kwargs):
        """
        This means we can initialize any number of arguments and
        keyword arguments
        Args:
            *args:   represent single unused arguments
            *kwargs: Are in dictionary form, meaning they are in key-value
               pairs
        """
        t_representation = "%Y-%m-%dT%H:%M:%S.%f"
        self.updated_at = datetime.today()
        self.created_at = datetime.today()
        self.id = str(uuid4())
        if len(kwargs) != 0:
            for key, value in kwargs:
                if key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.strptime(value, t_representation)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)
        
    def save(self):
        """update and save the value of the updated_at
        variable with current time that it has been saved"""
        self.updated_at = datetime.today()
        models.storage.save()
    
    def __str__(self):
        """Represents the string representation of our
        mighty base class"""
        class_name = type(self).__name__
        dict_representation = self.__dict__
        Identifier = self.id
        return "[{}] ({}) {}".\
            format(class_name, Identifier, dict_representation)
    
    def to_dict(self):
        """Represents a dictionary that specifies the meaning of our
        class variables and thier content"""
        class_dict = self.__dict__.copy()
        class_dict["__class__"] = self.__class__.__name__
        class_dict["created_at"] = class_dict["created_at"].isoformat()
        class_dict["updated_at"] = class_dict["updated_at"].isoformat()
        return class_dict