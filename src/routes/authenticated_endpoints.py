"""
This module defines authenticated endpoints that require user login.
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.review import Review
from ..models import db

authenticated_bp = Blueprint('authenticated_bp', __name__)


@authenticated_bp.route('/places/<int:place_id>/reviews', methods=['POST'])
@jwt_required()
def submit_review(place_id):
    """
    Endpoint for submitting a review for a place.

    Args:
        place_id (int): The ID of the place.

    Returns:
        JSON: A response indicating the result of the operation.
    """
    user_id = get_jwt_identity()
    data = request.get_json()
    review = Review(text=data['text'], place_id=place_id, user_id=user_id)
    db.session.add(review)
    db.session.commit()
    return jsonify(review.to_dict()), 201


@authenticated_bp.route('/places/<int:place_id>/reviews/<int:review_id>',
                        methods=['PUT'])
@jwt_required()
def edit_review(place_id, review_id):
    """
    Endpoint for editing a review.

    Args:
        place_id (int): The ID of the place.
        review_id (int): The ID of the review.

    Returns:
        JSON: A response indicating the result of the operation.
    """
    user_id = get_jwt_identity()
    data = request.get_json()
    review = Review.query.filter_by(id=review_id,
                                    place_id=place_id,
                                    user_id=user_id).first()
    if review:
        review.text = data['text']
        db.session.commit()
        return jsonify(review.to_dict()), 200
    else:
        return jsonify({"msg": "Review not found"}), 404


@authenticated_bp.route('/places/<int:place_id>/reviews/<int:review_id>',
                        methods=['DELETE'])
@jwt_required()
def delete_review(place_id, review_id):
    """
    Endpoint for deleting a review.

    Args:
        place_id (int): The ID of the place.
        review_id (int): The ID of the review.

    Returns:
        JSON: A response indicating the result of the operation.
    """
    user_id = get_jwt_identity()
    review = Review.query.filter_by(id=review_id,
                                    place_id=place_id,
                                    user_id=user_id).first()
    if review:
        db.session.delete(review)
        db.session.commit()
        return jsonify({"msg": "Review deleted successfully"}), 200
    else:
        return jsonify({"msg": "Review not found"}), 404
