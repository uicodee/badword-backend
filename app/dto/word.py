from pydantic import Field, BaseModel

from app.dto import Base


class Word(Base):

    word: str
    is_checked: bool = Field(alias="isChecked")


class PaginatedWord(BaseModel):
    words: list[Word]
    total_items: int
    pages: int
