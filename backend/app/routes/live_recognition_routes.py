"""Live recognition routes."""

from flask import Blueprint
from app.utils.response_utils import success_response

live_recognition_bp = Blueprint("live_recognition_bp", __name__)

@live_recognition_bp.route("/api/recognize", methods=["POST"])
def recognize_live():
    return success_response("live recognition endpoint")
