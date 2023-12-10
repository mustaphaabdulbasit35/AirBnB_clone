#!/usr/bin/python3
"""This is the model that will enable
users to make reviews. good review guranteed for this
our good work:)"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class enables users to create review 
    Attributes:
        user_id: Uniquely identifies the person making the review
        place_id: The location/place being reviewed
        text: What is the person saying in this review?
    """
    user_id = ""
    place_id = ""
    text = ""
