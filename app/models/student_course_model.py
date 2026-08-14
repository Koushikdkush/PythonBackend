import uuid
from sqlalchemy import ForeignKey, Integer, String, UUID, Column, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.connection import Base

student_course = Table(
    "student_course",
    Base.metadata,
    Column(
        "student_id",
        UUID(as_uuid=True),
        ForeignKey("student.id"),
        primary_key=True
    ),
    Column(
        "course_id",
        UUID(as_uuid=True),
        ForeignKey("course.id"),
        primary_key=True
    )
)


class Student(Base):
    __tablename__ = "student"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(String(100), nullable=True)

    courses = relationship(
        "Course",
        secondary=student_course,
        back_populates="students"
    )


class Course(Base):
    __tablename__ = "course"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(String(100), nullable=True)

    students = relationship(
        "Student",
        secondary=student_course,
        back_populates="courses"
    )