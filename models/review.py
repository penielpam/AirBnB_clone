#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review."""

    def __init__(self, place_id="", user_id="", text=""):
        """Initialize Review instance.

        Args:
            place_id (str): The Place id.
            user_id (str): The User id.
            text (str): The text of the review.
        """
        super().__init__()
        self.place_id = place_id
        self.user_id = user_id
        self.text = text

    def __str__(self):
        """Return a string representation of the Review instance."""
        return f"Review({self.place_id}, {self.user_id}, {self.text})"
