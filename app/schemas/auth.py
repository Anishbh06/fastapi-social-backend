from pydantic import BaseModel, EmailStr, constr
from datetime import datetime
from pydantic import ConfigDict

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    
class MeResponse(BaseModel):
    id: int
    email: str
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)