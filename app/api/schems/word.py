from pydantic import BaseModel, Field


class Word(BaseModel):

    word: str


class UpdateWord(BaseModel):

    word_id: int = Field(alias="wordId")
    is_checked: bool = Field(alias="isChecked")
