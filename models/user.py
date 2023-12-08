#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User."""

    def __init__(self, email="", password="", first_name="", last_name=""):
        """Initialize User instance.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
        """
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        """Return a string representation of the User instance."""
        return f"User({self.email}, {self.password}, {self.first_name},
              {self.last_name})"
