from .database import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Place(db.Model):
    __tablename__ = 'place'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    host_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    host = relationship("User", back_populates="places")
    reviews = relationship("Review", back_populates="place")