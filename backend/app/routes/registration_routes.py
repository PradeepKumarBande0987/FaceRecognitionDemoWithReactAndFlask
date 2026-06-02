"""Registration routes."""

from flask import Blueprint, jsonify, request
from app.extensions import db
from app.models.person import Person
from app.utils.response_utils import success_response, error_response

registration_bp = Blueprint("registration_bp", __name__)

@registration_bp.route("/api/register", methods=["POST"])
def register_person():
    data = request.get_json()

    if not data:
        return error_response("No data received!", 400)
    
    full_name = data.get("full_name","").strip()

    if not full_name:
        return error_response("Full name is required!", 400)
    
    existing_person = Person.query.filter_by(full_name=full_name).first()

    if existing_person:
        return error_response("Person already exists.", 400)
    
    person = Person(full_name=full_name)
    db.session.add(person)
    db.session.commit()

    return success_response("Person regustered successfully.", person.to_dict(),201)