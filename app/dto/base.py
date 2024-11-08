from datetime import datetime

from pydantic import BaseModel, Field


def serialize_time(value: datetime) -> str:
    return value.strftime("%d.%m.%Y %H:%M")


class Base(BaseModel):
    id: int
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")

    class Config:
        json_encoders = {datetime: serialize_time}
        from_attributes = True
        populate_by_name = True
