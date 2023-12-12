#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User entity.

    Attributes:
        email (str): The email address associated with the user.
        password (str): The secure password for user authentication.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    def __init__(self, *args, **kwargs):
        """Initialize User instance."""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
