from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status


def create_user(db: Session, user_in: UserCreate) -> User:
    hashed = hash_password(user_in.password)

    user = User(
        email=user_in.email,
        hashed_password=hashed
    )

    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    db.refresh(user)
    return user

