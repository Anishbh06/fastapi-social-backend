from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post import PostCreate

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