"""
User-related routes and controller functions.
"""

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from src.models.user import User
from src.models import db

users_bp = Blueprint('users_bp', __name__)


@users_bp.route('/users', methods=['POST'])
def create_user():
    """
    Creates a new user.
    """
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(email=email).first():
        return jsonify({"msg": "User already exists"}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(email=email, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201


@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Updates an existing user.
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({"msg": "User not found"}), 404

    data = request.get_json()
    user.email = data.get('email', user.email)
    password = data.get('password')
    if password:
        user.password_hash = generate_password_hash(password)

    db.session.commit()

    return jsonify(user.to_dict()), 200


@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Deletes an existing user.
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({"msg": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"msg": "User deleted"}), 200
