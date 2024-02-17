from typing import Optional

from pydantic import BaseModel
from datetime import datetime

class CirculationDomainModel(BaseModel):
    id: Optional[int] = -1
    member_id: Optional[int] = None
    book_id: int
    issue_date: Optional[datetime] = None
    return_date: Optional[datetime] = None

    class Config:
        from_attributes = True



class ReservationDomainModel(BaseModel):
    id: Optional[int] = -1
    member_id: int
    book_id: int
    is_active: bool = True
    date: Optional[datetime] = None

    class Config:
        from_attributes = True