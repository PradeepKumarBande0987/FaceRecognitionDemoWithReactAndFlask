"""Live recognition routes."""

from flask import Blueprint, jsonify

live_recognition_bp = Blueprint("live_recognition", __name__)

@live_recognition_bp.route("/recognize", methods=["POST"])
def recognize_live():
    return jsonify({"message": "live recognition endpoint"})
