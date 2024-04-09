from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.models import BaseModel


class Word(BaseModel):
    __tablename__ = "word"

    word: Mapped[str] = mapped_column(String)
    is_checked: Mapped[bool] = mapped_column(default=False)
