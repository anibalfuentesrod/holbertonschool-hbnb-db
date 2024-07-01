""""docstring here aahh"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

# Import the config classes
from src.config import DevelopmentConfig, TestingConfig, ProductionConfig
from src.models.user import User

# Load environment variables from .env file if it exists
load_dotenv()

# Initialize the database
db = SQLAlchemy()


def create_app(config_name):
    """
    Create and configure the Flask app.
    """
    app = Flask(__name__)

    if config_name == "development":
        app.config.from_object(DevelopmentConfig)
    elif config_name == "test":
        app.config.from_object(TestingConfig)
    elif config_name == "production":
        app.config.from_object(ProductionConfig)
    else:
        raise ValueError("Invalid configuration name")

    print("Using configuration:", config_name)
    print("Database URI:", app.config['SQLALCHEMY_DATABASE_URI'])

    app.config['SQLALCHEMY_ECHO'] = True  # Enable SQLAlchemy logging

    # Initialize app with database
    db.init_app(app)
    Migrate(app, db)

    # Setup JWT
    jwt = JWTManager(app)

    # Register blueprints
    from src.routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/')

    # Create test user for authentication in tests
    with app.app_context():
        if config_name == "test":
            db.create_all()
            test_user = User(email='test@example.com', is_admin=True)
            test_user.set_password('test')
            db.session.add(test_user)
            db.session.commit()

    return app
