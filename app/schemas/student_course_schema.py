from pydantic import BaseModel
from uuid import UUID


class StudentShape(BaseModel):
    id: UUID
    name: str | None = None
    courses: list[CourseShape] = []


    class Config:
        from_attributes = True

class CourseShape(BaseModel):
    id: UUID
    name: str | None = None
    students: list[StudentShape] = []

    class Config:
        from_attributes = True


class StudentCreate(BaseModel):
    name: str

class CourseCreate(BaseModel):
    name: str


class StudentResponse(BaseModel):
    id: UUID
    name: str | None = None
    courses: list[CourseShape] = []

    class Config:
        from_attributes = True


class CourseResponse(BaseModel):
    id: UUID
    name: str | None = None
    students: list[StudentShape] = []

    class Config:
        from_attributes = True