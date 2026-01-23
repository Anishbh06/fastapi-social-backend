from fastapi import APIRouter, Depends, Query, status, HTTPException
from sqlalchemy.orm import Session
from typing import List


from app.database.database import SessionLocal
from app.schemas.post import PostCreate, PostResponse
from app.crud.post import create_post, get_posts, get_my_posts, delete_post
from app.core.security import get_current_user
from app.models.user import User
from app.database.deps import get_db
from app.schemas.post import PostUpdate
from app.crud.post import update_post



router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post("/", response_model=PostResponse)
def create_new_post(
    post: PostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_post(db, post, current_user.id)


@router.get("/", response_model=List[PostResponse])
def read_posts(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return get_posts(db, skip=skip, limit=limit)

@router.get("/me", response_model=list[PostResponse])
def read_my_posts(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_my_posts(
        db,
        user_id=current_user.id,
        skip=skip,
        limit=limit,
    )


@router.put("/{post_id}", response_model=PostResponse)
def edit_post(
    post_id: int,
    post: PostUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return update_post(
        db=db,
        post_id=post_id,
        post_in=post,
        user_id=current_user.id,
    )


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_own_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    deleted = delete_post(
        db,
        post_id=post_id,
        user_id=current_user.id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found or not owned by you",
        )