"""
Module for authentication routes.
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.models.user import User, db

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Register a new user.
    """
    data = request.get_json()
    user = User.create(data)
    return jsonify(user.to_dict()), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Log in an existing user.
    """
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id, additional_claims={"is_admin": user.is_admin})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad email or password"}), 401

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    """
    Access a protected route.
    """
    current_user = get_jwt_identity()
    return jsonify(message="This is a protected route", user=current_user), 200

@auth_bp.route('/promote_user', methods=['POST'])
@jwt_required()
def promote_user():
    """
    Promote a user to admin.
    """
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)

    if not current_user or not current_user.is_admin:
        return jsonify({'message': 'Access forbidden'}), 403

    data = request.get_json()
    email = data.get('email')
    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({'message': 'User not found'}), 404

    user.is_admin = True
    db.session.commit()

    return jsonify({'message': 'User promoted to admin'}), 200