from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import db

class Place(db.Model):
    __tablename__ = 'place'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    host_id = Column(Integer, ForeignKey('user.id'))
    price = Column(Integer, nullable=False)

    host = relationship("User", back_populates="places")
    reviews = relationship("Review", back_populates="place")