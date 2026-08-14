from sqlalchemy.orm import Session,selectinload
from fastapi import *
from app.models.posts_model import Post
from app.schemas.post_schema import PostCreate,PostResponse
import uuid

# getAll Post
def getAllPosts(db:Session):
    return db.query(Post).all()

# get postByUserId

def getPostByUserId(db:Session, userId: uuid.UUID):
    return db.query(Post).options(selectinload(Post.user)).filter(
        Post.user_id == userId
    ).all()

# get postById
def getPostById(db:Session,postId: uuid.UUID):
    return db.query(Post).filter(
        Post.id == postId
    ).first()

# create post
def createPost(db:Session,payload:PostCreate):
    try:
        newPost = Post(
            title=payload.title,
            user_id=payload.user_id
        )
        db.add(newPost)
        db.commit()
        db.refresh(newPost)
        return newPost
    
    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(status_code=500,detail="Internal server error!")