"""Health check routes."""

from flask import Blueprint
from app.utils.response_utils import success_response

health_bp = Blueprint("health_bp", __name__)

@health_bp.route("/api/health", methods=["GET"])
def health_check():
    return success_response("Backend is running successfully")
