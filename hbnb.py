from flask import Flask
from src.models import init_app
from src.routes.users import users_bp
import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True  # Enable SQLAlchemy logging
    init_app(app)
    app.register_blueprint(users_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)