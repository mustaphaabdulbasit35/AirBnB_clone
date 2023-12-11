#!/usr/bin/python3
"""
model specifies the city  that the user wants to explore
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This class is used to manage subsequent city objetcs that will be created
    Attributes:
        state_id(str): Uniquely identifies a given state
        name(str): represents the naming of the city
    """
    
    state_id = ""
    name = ""