
import uuid

from sqlalchemy import UUID, Column, ForeignKey, String
from app.database.connection import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )    
    title = Column(String)
    user_id = Column(ForeignKey("users.id"))
    user = relationship("User", back_populates="posts")