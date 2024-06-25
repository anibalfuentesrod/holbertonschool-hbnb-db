from .database import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Review(db.Model):
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True)
    content = Column(String(500), nullable=False)
    place_id = Column(Integer, ForeignKey('place.id'), nullable=False)
    place = relationship("Place", back_populates="reviews")