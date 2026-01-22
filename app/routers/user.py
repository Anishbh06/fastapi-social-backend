from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.deps import get_db
from app.schemas.user import UserCreate, UserResponse
from app.crud.user import create_user
from app.core.security import get_current_user          

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/",response_model=UserResponse,status_code=status.HTTP_201_CREATED,)
def register_user(user: UserCreate,db: Session = Depends(get_db),):
    return create_user(db, user)


@router.get("/protected-test")
def protected_test(current_user=Depends(get_current_user)):
    return {
        "message": "You are authenticated",
        "user_id": current_user.id,
        "email": current_user.email,
    }
