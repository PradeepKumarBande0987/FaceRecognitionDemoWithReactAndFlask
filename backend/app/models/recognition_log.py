"""Recognition log model."""

class RecognitionLog:
    def __init__(self, person_id: int, timestamp: str, confidence: float):
        self.person_id = person_id
        self.timestamp = timestamp
        self.confidence = confidence
