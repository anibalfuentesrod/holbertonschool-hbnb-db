"""
This module defines the City model.
"""

from sqlalchemy import Column, String, ForeignKey
from .base import Base


class City(Base):
    """
    Represents a City in the application.

    Attributes:
        name (str): The name of the city.
        country_id (int): The ID of the country the city belongs to.
    """
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    country_id = Column(String(60), ForeignKey('countries.id'), nullable=False)

    def __repr__(self):
        """
        Provides a string representation of the City object.

        Returns:
            str: The string representation of the City object.
        """
        return f'<City(name={self.name}, country_id={self.country_id})>'
