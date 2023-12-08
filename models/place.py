#!/usr/bin/python3
"""Defines the City class."""

from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city."""

    def __init__(self, state_id="", name=""):
        """Initialize City instance.

        Args:
            state_id (str): The state id.
            name (str): The name of the city.
        """
        super().__init__()
        self.state_id = state_id
        self.name = name

    def __str__(self):
        """Return a string representation of the City instance."""
        return f"City({self.state_id}, {self.name})"
