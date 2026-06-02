"""Face encoding model."""
from datetime import datetime
from app.extensions import db

class FaceEncoding(db.Model):
    __tablename__ = "face_encodings"

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"), nullable=False)
    image_path = db.Column(db.String(255), nullable=False)
    encoding_path = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "person_id": self.person_id,
            "image_path": self.image_path,
            "encoding_path": self.encoding_path,
            "created_at": self.created_at.isoformat()
        }
