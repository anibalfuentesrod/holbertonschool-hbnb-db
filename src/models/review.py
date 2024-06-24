from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import db

class Review(db.Model):
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    place_id = Column(Integer, ForeignKey('place.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", back_populates="reviews")
    place = relationship("Place", back_populates="reviews")