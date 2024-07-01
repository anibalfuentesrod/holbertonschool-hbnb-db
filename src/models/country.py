"""
This module defines the Country model.
"""

from sqlalchemy import Column, String
from .base import Base


class Country(Base):
    """
    Represents a Country in the application.

    Attributes:
        name (str): The name of the country.
    """
    __tablename__ = 'countries'

    name = Column(String(128), nullable=False)

    def __repr__(self):
        """
        Provides a string representation of the Country object.

        Returns:
            str: The string representation of the Country object.
        """
        return f'<Country(name={self.name})>'
