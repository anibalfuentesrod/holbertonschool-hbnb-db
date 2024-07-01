"""
This module defines user-related endpoints.
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash
from ..models.user import User
from ..models import db

users_bp = Blueprint('users_bp', __name__)

@users_bp.route('/users', methods=['POST'], strict_slashes=False)
@jwt_required()
def create_user():
    """
    Endpoint for creating a new user.

    Returns:
        JSON: A response indicating the result of the operation.
    """
    data = request.get_json()
    user = User.create(data)
    return jsonify(user.to_dict()), 201

@users_bp.route('/users/<int:user_id>/', methods=['PUT'], strict_slashes=False)
@jwt_required()
def update_user(user_id):
    """
    Endpoint for updating an existing user.

    Args:
        user_id (int): The ID of the user.

    Returns:
        JSON: A response indicating the result of the operation.
    """
    data = request.get_json()
    user = User.query.get(user_id)
    if user:
        user.email = data.get('email', user.email)
        user.is_admin = data.get('is_admin', user.is_admin)
        if 'password' in data:
            user.password_hash = generate_password_hash(data['password'])
        db.session.commit()
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({"msg": "User not found"}), 404

@users_bp.route('/users/<int:user_id>/', methods=['DELETE'], strict_slashes=False)
@jwt_required()
def delete_user(user_id):
    """
    Endpoint for deleting a user.

    Args:
        user_id (int): The ID of the user.

    Returns:
        JSON: A response indicating the result of the operation.
    """
    user = User.query.get(user_id)
    if user:
        # Detach the user object from the current session
        db.session.expunge(user)
        # Attach the user object to the new session for deletion
        user = db.session.merge(user)
        db.session.delete(user)
        db.session.commit()
        return jsonify({"msg": "User deleted successfully"}), 200
    else:
        return jsonify({"msg": "User not found"}), 404

@users_bp.route('/users/<int:user_id>/', methods=['GET'], strict_slashes=False)
@jwt_required()
def get_user(user_id):
    """
    Endpoint for fetching a single user by ID.

    Args:
        user_id (int): The ID of the user.

    Returns:
        JSON: The user data or a 404 error if not found.
    """
    user = User.query.get(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({"msg": "User not found"}), 404

@users_bp.route('/users/', methods=['GET'], strict_slashes=False)
@jwt_required()
def get_users():
    """
    Endpoint for fetching all users.

    Returns:
        JSON: A list of all users.
    """
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200