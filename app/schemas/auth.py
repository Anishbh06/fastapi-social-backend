from pydantic import BaseModel, EmailStr, constr
from datetime import datetime
from pydantic import ConfigDict


class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"