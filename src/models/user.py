"""
This module defines the User model.
"""

from werkzeug.security import generate_password_hash, check_password_hash
from .database import db


class User(db.Model):
    """
    User model for storing user details.
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        """
        Set the password for the user.

        Args:
            password (str): The password to be set.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Check if the provided password matches the stored password hash.

        Args:
            password (str): The password to be checked.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def create(data):
        """
        Create a new user.

        Args:
            data (dict): The user data.

        Returns:
            User: The created user.
        """
        user = User(
            email=data['email'],
            password_hash=generate_password_hash(data['password']),
            is_admin=data.get('is_admin', False)
        )
        db.session.add(user)
        db.session.commit()
        return user

    def to_dict(self):
        """
        Convert the user object to a dictionary.

        Returns:
            dict: The user data as a dictionary.
        """
        return {
            'id': self.id,
            'email': self.email,
            'is_admin': self.is_admin
        }
