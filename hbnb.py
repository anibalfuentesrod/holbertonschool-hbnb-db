from flask import Flask
from src.models import init_app, db
import os
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from src.routes.auth import auth_bp

# Load environment variables from .env file if it exists
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True  # Enable SQLAlchemy logging
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')  # Set up JWT secret key

    # Initialize app with database
    init_app(app)

    # Setup Flask-Migrate
    migrate = Migrate(app, db)

    # Setup JWT
    jwt = JWTManager(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5002, debug=True)