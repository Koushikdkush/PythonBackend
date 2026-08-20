import datetime
import uuid
from sqlalchemy import Integer, String, UUID, Float, Column, Boolean, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.connection import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int] = mapped_column(Integer)
    salary: Mapped[float] = mapped_column(Float)
    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        index=True
    )
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    address = Column(String(100), nullable=True)
    role: Mapped[str] = mapped_column(String(100), nullable=True, default='User')
    date_of_birth: Mapped[datetime.date | None] = mapped_column(Date, nullable=True)
    phoneNumber = Column(String(10), nullable=True)
    isActive: Mapped[bool] = mapped_column(Boolean,default=True, nullable=True)
    idDeleted: Mapped[bool] = mapped_column(Boolean,default=False, nullable=True)
    posts = relationship("Post", back_populates="user")

