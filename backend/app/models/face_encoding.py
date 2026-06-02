"""Face encoding model."""

class FaceEncoding:
    def __init__(self, person_id: int, encoding: list[float]):
        self.person_id = person_id
        self.encoding = encoding
