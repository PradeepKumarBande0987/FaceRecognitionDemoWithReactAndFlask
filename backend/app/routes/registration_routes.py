"""Registration routes."""

from flask import Blueprint, jsonify

registration_bp = Blueprint("registration", __name__)

@registration_bp.route("/register", methods=["POST"])
def register_person():
    return jsonify({"message": "registration endpoint"})
