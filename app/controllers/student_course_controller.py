from fastapi import HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.schemas.student_course_schema import StudentCreate,CourseCreate
from app.services import student_course_service


def getAllCourses(db:Session):
    return student_course_service.getAllCourse(db)

def getAllStudents(db:Session):
    return student_course_service.getAllStudents(db)

def createStudent(db:Session,payload: StudentCreate):
    response = student_course_service.createStudent(db,payload)
    return response

def createCourse(db:Session,payload: CourseCreate):
    response = student_course_service.createCourse(db,payload)
    return response

def enrollStudentToCourse(db:Session,studentId:UUID,courseId:list[UUID]):
    response = student_course_service.enrollStudentToCourse(db,studentId,courseId)
    return response

def courseEnrolled(db: Session,studentId: UUID):
    response = student_course_service.courseEnrolled(db,studentId)
    return response

def studentEnrolled(db:Session,courseId: UUID):
    response = student_course_service.studentEnrolled(db,courseId)
    return response