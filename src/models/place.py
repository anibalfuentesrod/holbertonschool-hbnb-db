"""
Place Model.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base


class Place(Base):
    """
    Represents a place in the database.
    """
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    city_id = Column(Integer, ForeignKey('cities.id'))

    def __init__(self, name, description, user_id, city_id):
        """
        Initializes a new place.
        """
        self.name = name
        self.description = description
        self.user_id = user_id
        self.city_id = city_id
