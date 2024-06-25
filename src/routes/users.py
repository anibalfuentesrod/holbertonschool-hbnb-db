from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.controllers.users import get_users, create_user

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/', methods=['GET'], strict_slashes=False)
@jwt_required()
def users_get():
    return jsonify(get_users())

@users_bp.route('/', methods=['POST'], strict_slashes=False)
@jwt_required()
def users_post():
    current_user = get_jwt_identity()
    if current_user['is_admin']:
        data = request.get_json()
        create_user(data)
        return jsonify({"message": "User created successfully"}), 201
    return jsonify({"msg": "Admins only!"}), 403