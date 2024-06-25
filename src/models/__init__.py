from .database import db
from .user import User
from .place import Place
from .review import Review

def init_app(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()  # Create tables if they don't exist

__all__ = ['db', 'User', 'Place', 'Review']