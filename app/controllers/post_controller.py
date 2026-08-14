from fastapi import HTTPException
from sqlalchemy.orm import Session
import uuid
from app.schemas.post_schema import *
from app.services import post_service

def getAllPosts(db:Session):
    return post_service.getAllPosts(db)

def getPostById(db:Session,postId: uuid.UUID):
    response = post_service.getPostById(db,postId)

    if response is None:
        raise HTTPException(status_code=404,detail="Post not found!")

    return response

def create_post(db:Session,payload:PostCreate):
    response = post_service.createPost(db,payload)
    return response

def getPostByUserId(db:Session, userId: uuid.UUID):
    response = post_service.getPostByUserId(db,userId)
    return response
