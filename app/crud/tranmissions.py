from sqlalchemy.orm import Session
from app.models.transmissions import Transmission
from typing import List

def get_all_transmissions(db: Session) -> List[Transmission]:
    return db.query(Transmission).all()