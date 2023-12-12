#!/usr/bin/python3
"""Module for the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """A class that represents a state.

    Attributes:
        name (str): The name of the state.
    """

    # Initialize an empty string for the state name
    name = ""
