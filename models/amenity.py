#!/usr/bin/python3
"""Amenity class definition."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class representing an amenity.

    Attributes:
        name (str): The amenity's name.
    """

    name = ""
