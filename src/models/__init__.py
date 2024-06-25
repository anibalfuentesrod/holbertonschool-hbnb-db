from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .place import Place
from .review import Review

def init_app(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

__all__ = ['db', 'User', 'Place', 'Review']