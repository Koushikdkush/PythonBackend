from sqlalchemy.orm import Session
from app.models.student_course_model import *
from app.schemas.student_course_schema import *
from fastapi import HTTPException
import uuid


def getAllCourse(db:Session):
    return db.query(Course).all()

def getAllStudents(db:Session):
    return db.query(Student).all()


def createStudent(db:Session,payload:StudentCreate):
    existingStudent = db.query(Student).filter(
        Student.name == payload.name
    ).first()

    if existingStudent is not None:
        raise HTTPException(status_code=400,detail="Student already exists")

    newStudent = Student(
        name=payload.name
    )

    db.add(newStudent)
    db.commit()
    db.refresh(newStudent)
    return newStudent


def createCourse(db:Session,payload: CourseCreate):
    existingCourse = db.query(Course).filter(
        Course.name == payload.name
    ).first()

    if existingCourse is not None:
        raise HTTPException(status_code=400,detail="Course already exists")

    newCourse = Course(
        name=payload.name
    )

    db.add(newCourse)
    db.commit()
    db.refresh(newCourse)
    return newCourse

def courseEnrolled(db:Session,studentId: UUID):
    student = db.query(Student).filter(
        Student.id == studentId
    ).first()

    if student is None:
        raise HTTPException(status_code=404,detail="Student not found!")
    
    return student.courses

def studentEnrolled(db:Session,courseId: UUID):

    try:
        course = db.query(Course).filter(
        Course.id == courseId
        ).first()

        if course is None:
            raise HTTPException(status_code=404,detail="Course not found!")

        return course.students
    
    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(status_code=500,detail="Internal server error")



def enrollStudentToCourse(
    db: Session,
    studentId: uuid.UUID,
    courseIds: list[uuid.UUID]
):
    student = db.query(Student).filter(
        Student.id == studentId
    ).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    for cr in courseIds:
        course = db.query(Course).filter(
        Course.id == cr).first()

        if course is None:
            raise HTTPException(status_code=404,
            detail="Course not found")

        if course in student.courses:
            raise HTTPException(status_code=400,detail="Student is already enrolled in this course")

        student.courses.append(course)

    db.commit()
    db.refresh(student)

    return student