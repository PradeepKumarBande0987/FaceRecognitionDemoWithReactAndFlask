"""Person model."""
from datetime import datetime
from app.extensions import db

class Person (db.Model): 
    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    face_encodings = db.relationship("FaceEncoding", backref="person", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "created_at": self.created_at.isoformat()
        }
