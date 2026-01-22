from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.deps import get_db
from app.schemas.auth import LoginRequest, TokenResponse, MeResponse
from app.crud.auth import authenticate_user
from app.core.security import create_access_token
from app.core.security import get_current_user
from app.models.user import User


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, data.email, data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    token = create_access_token({"user_id": user.id})

    return {"access_token": token}

@router.get("/me", response_model= MeResponse )
def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user