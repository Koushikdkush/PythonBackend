from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.post_schema import PostShape,PostResponse,PostCreate
from app.controllers import post_controller
import uuid

router = APIRouter(
    prefix="/posts",tags=["Posts"]
)


@router.get("/",response_model=list[PostResponse])
def getAllPosts(db:Session = Depends(get_db)):
    return post_controller.getAllPosts(db)

@router.get("/{postId}", response_model=PostResponse)
def getPostById(postId: uuid.UUID,db:Session = Depends(get_db)):
    return post_controller.getPostById(db,postId)

@router.post("/createPost",response_model=PostResponse)
def createPost(payload:PostCreate,db:Session = Depends(get_db)):
    return post_controller.create_post(db,payload)

@router.get("/userPosts/{userId}", response_model=list[PostShape])
def getPostsByUserId(userId: uuid.UUID,db: Session = Depends(get_db)):
    return post_controller.getPostByUserId(db,userId)