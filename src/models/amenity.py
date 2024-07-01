"""
This module defines the Amenity model.
"""

from sqlalchemy import Column, String
from .base import Base


class Amenity(Base):
    """
    Represents an Amenity in the application.

    Attributes:
        name (str): The name of the amenity.
    """
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    def __repr__(self):
        """
        Provides a string representation of the Amenity object.

        Returns:
            str: The string representation of the Amenity object.
        """
        return f'<Amenity(name={self.name})>'
