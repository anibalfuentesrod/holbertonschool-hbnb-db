from flask import Blueprint, request, jsonify
from src.controllers.users import get_users, create_user

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/', methods=['GET'], strict_slashes=False)
def users_get():
    return jsonify(get_users())

@users_bp.route('/', methods=['POST'], strict_slashes=False)
def users_post():
    data = request.get_json()
    create_user(data)
    return jsonify({"message": "User created successfully"}), 201