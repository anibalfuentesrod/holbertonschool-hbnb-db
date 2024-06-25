from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import db

class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    is_admin = Column(Integer, default=0)
    places = relationship("Place", back_populates="host")

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'is_admin': self.is_admin
        }

    @staticmethod
    def create(data):
        user = User(
            email=data['email'],
            password=data['password'],
            is_admin=data.get('is_admin', 0)
        )
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_all():
        return [user.to_dict() for user in User.query.all()]