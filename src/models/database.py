"""
This module defines the database configuration and models for the application.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    """
    Base model class that includes common attributes.
    """
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
