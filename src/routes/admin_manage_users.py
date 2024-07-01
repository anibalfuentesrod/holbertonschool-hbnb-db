"""
This module defines the admin user management endpoints.
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from ..models.user import User
from ..models import db

admin_manage_users_bp = Blueprint('admin_manage_users_bp', __name__)


@admin_manage_users_bp.route('/admin/users', methods=['POST'])
@jwt_required()
def promote_user():
    """
    Endpoint to promote a user to admin.

    Returns:
        JSON: A response indicating the result of the operation.
    """
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Administration rights required"}), 403

    data = request.get_json()
    user_id = data.get('user_id')
    user = User.query.get(user_id)
    if user:
        user.is_admin = True
        db.session.commit()
        return jsonify({"msg": "User promoted to admin successfully"}), 200
    else:
        return jsonify({"msg": "User not found"}), 404
