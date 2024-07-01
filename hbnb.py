"""
This module initializes and runs the Flask application.
"""

from flask import Flask, request, jsonify
from src.models import init_app, db
import os
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from src.routes.auth import auth_bp
from src.models.user import User

# Load environment variables from .env file if it exists
load_dotenv()

def create_app():
    """
    Creates and configures the Flask application.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True  # Enable SQLAlchemy logging
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    # Initialize app with database
    init_app(app)

    # Setup Flask-Migrate
    migrate = Migrate(app, db)

    # Setup JWT
    jwt = JWTManager(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/')

    # Define CRUD routes
    @app.route('/users/', methods=['POST'])
    def create_user():
        data = request.get_json()
        new_user = User(email=data['email'], is_admin=False)
        new_user.set_password(data['password'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201

    @app.route('/users/', methods=['GET'])
    def get_users():
        users = User.query.all()
        return jsonify([user.to_dict() for user in users])

    @app.route('/users/<int:id>/', methods=['GET'])
    def get_user(id):
        user = User.query.get_or_404(id)
        return jsonify(user.to_dict())

    @app.route('/users/<int:id>/', methods=['PUT'])
    def update_user(id):
        data = request.get_json()
        user = User.query.get_or_404(id)
        user.email = data['email']
        user.set_password(data['password'])
        db.session.commit()
        return jsonify(user.to_dict())

    @app.route('/users/<int:id>/', methods=['DELETE'])
    def delete_user(id):
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted'})

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)