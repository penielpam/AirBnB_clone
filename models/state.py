#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state."""

    def __init__(self, name=""):
        """Initialize State instance.

        Args:
            name (str): The name of the state.
        """
        super().__init__()
        self.name = name

    def __str__(self):
        """Return a string representation of the State instance."""
        return f"State({self.name})"
