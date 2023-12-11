#!/usr/bin/python3
"""
Module to represent the various amenities that
customers visiting AirBnB can explore
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This class defines the amenities module
    """
    
    name = ""