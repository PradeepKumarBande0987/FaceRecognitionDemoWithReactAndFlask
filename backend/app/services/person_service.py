"""Person service."""

def person_service(person):
     return {
        "id": person.id,
        "full_name": person.full_name,
        "created_at": person.created_at.isoformat()
    }
