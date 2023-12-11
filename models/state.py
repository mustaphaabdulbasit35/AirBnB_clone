#!/usr/bin/python3
"""
MOdule to precise the state inhich the AIRBNB
is located
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Class which enables the creation of object
      representtions of various possible states
    Attribute:
        name(str): The string representaion of state name
    """
    name = ""
