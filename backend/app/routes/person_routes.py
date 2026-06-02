"""Person-related routes."""

from flask import Blueprint, jsonify

person_bp = Blueprint("person", __name__)

@person_bp.route("/persons", methods=["GET"])
def get_persons():
    return jsonify([])
