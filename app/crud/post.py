from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post import PostCreate, PostUpdate
from fastapi import HTTPException, status

def create_post(db: Session, post_in: PostCreate, owner_id: int) -> Post:
    post = Post(
        title=post_in.title,
        content=post_in.content,
        owner_id=owner_id,
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return (
        db.query(Post)
        .order_by(Post.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_my_posts(
    db: Session,
    user_id: int,
    skip: int = 0,
    limit: int = 10,
):
    return (
        db.query(Post)
        .filter(Post.owner_id == user_id)
        .order_by(Post.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


def update_post(
    db: Session,
    post_id: int,
    post_in: PostUpdate,
    user_id: int,
):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found",
        )

    if post.owner_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this post",
        )

    if post_in.title is not None:
        post.title = post_in.title

    if post_in.content is not None:
        post.content = post_in.content

    db.commit()
    db.refresh(post)
    return post


def delete_post(db: Session, post_id: int, user_id: int) -> Post | None:
    post = (
        db.query(Post)
        .filter(Post.id == post_id, Post.owner_id == user_id)
        .first()
    )

    if not post:
        return None

    db.delete(post)
    db.commit()
    return post