"""init th file app haha"""
from flask_sqlalchemy import SQLAlchemy
from .user import User
db = SQLAlchemy()


def init_app(app):
    """and in here tooo hahh"""
    db.init_app(app)


__all__ = ['User']
