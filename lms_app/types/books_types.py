from pydantic import BaseModel


class BookDomainModel(BaseModel):
    id: int
    book_name: str
    available_copies: int
    total_copies: int = 0

    class Config:
        # orm_mode = True
        from_attributes = True