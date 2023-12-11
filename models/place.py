#!/usr/bin/python3
"""
This module is used to further precise location,
 enabling the craetion of place objects
 """
from models.base_model import BaseModel


class Place(BaseModel):
    """
    This class creates and manages place objects
    Note that the values below are initialized ones.
    Attributes:
        city_id (str): identifier for the city
        user_id (str): uniquely identifies user
        name (str): represents the name of the place
        max_guest (int): the max accomodation capacity
        price_by_night (int): How much it costs per night
        latitude (float): geographical latitudinal description
        longitude (float): geographical longitudinal description
        amenity_ids (list): the thing we can enjoy, their IDs
        description (str): instance used to describe the place
        number_rooms (int): shows the number of rooms in the place
        number_bathrooms (int): bathroom amount/number.
    """
    
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    city_id = ""
    user_id = ""
    name = ""
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []