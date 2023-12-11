#!/usr/bin/python3
"""
Module to enable the creation of various AIRBNB users
"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class enables us to create various user objects
    or users, each time someone visits.
      Each user is uniquely identified
    Attributes:
        first_name: The users first name
        last_name: represents the users last name
        email: The visiting users email
        password: The users UNIQUE password
      """
    
    first_name = ""
    last_name = ""
    email = ""
    password = ""