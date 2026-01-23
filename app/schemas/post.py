from pydantic import BaseModel
from datetime import datetime
from pydantic import ConfigDict
from typing import Optional

class PostCreate(BaseModel):
    title: str
    content: str


class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    owner_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None