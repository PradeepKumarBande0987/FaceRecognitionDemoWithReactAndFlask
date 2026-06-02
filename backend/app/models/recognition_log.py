"""Recognition log model."""
from datetime import datetime
from app.extensions import db

class RecognitionLog(db.Model):
    __tablename__ = "recognition_logs"

    id = db.Column(db.Integer, primary_key=True)
    detected_name = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "detected_name": self.detected_name,
            "status": self.status,
            "created_at": self.created_at.isoformat()
        }
