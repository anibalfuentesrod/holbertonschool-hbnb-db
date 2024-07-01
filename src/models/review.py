"""
Review Model.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base


class Review(Base):
    """
    Represents a review in the database.
    """
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    place_id = Column(Integer, ForeignKey('places.id'))

    def __init__(self, text, user_id, place_id):
        """
        Initializes a new review.
        """
        self.text = text
        self.user_id = user_id
        self.place_id = place_id
