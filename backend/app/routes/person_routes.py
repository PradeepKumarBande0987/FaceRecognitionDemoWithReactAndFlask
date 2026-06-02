"""Person-related routes."""

from flask import Blueprint, jsonify
from app.models.person import Person

person_bp = Blueprint("person_bp", __name__)

@person_bp.route("/api/persons", methods=["GET"])
def get_all_persons():
    persons = Person.query.order_by(Person.id.desc()).all()

    return jsonify({
        "success": True,
        "data": [persons.to_dict() for person in persons]
    })
