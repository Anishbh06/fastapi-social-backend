from pydantic import BaseModel, EmailStr, constr
from datetime import datetime
from pydantic import ConfigDict



class UserCreate(BaseModel):
    email: EmailStr
    password: constr(min_length=0, max_length=72)

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active : bool
    created_at : datetime

    model_config = ConfigDict(from_attributes=True)


