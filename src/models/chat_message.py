from fastapi.encoders import jsonable_encoder

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

from src.models.objectid import PydanticObjectId

class ChatMessage(BaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    user: str
    message: str
    timestamp: datetime

    def to_json(self):
        return jsonable_encoder(self, exclude_none=True)

    def to_bson(self):
        data = self.dict(by_alias=True, exclude_none=True)
        if data.get("_id") is None:
            data.pop("_id", None)
        return data