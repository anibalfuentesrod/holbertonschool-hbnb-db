"""
This module defines public endpoints that do not require user login.
"""

from flask import Blueprint, jsonify
from ..models.place import Place

public_bp = Blueprint('public_bp', __name__)


@public_bp.route('/places', methods=['GET'])
def view_places():
    """
    Endpoint for viewing all places.

    Returns:
        JSON: A response containing all places.
    """
    places = Place.query.all()
    return jsonify([place.to_dict() for place in places]), 200


@public_bp.route('/places/<int:place_id>', methods=['GET'])
def view_place_details(place_id):
    """
    Endpoint for viewing the details of a specific place.

    Args:
        place_id (int): The ID of the place.

    Returns:
        JSON: A response containing the details of the place.
    """
    place = Place.query.get(place_id)
    if place:
        return jsonify(place.to_dict()), 200
    else:
        return jsonify({"msg": "Place not found"}), 404
