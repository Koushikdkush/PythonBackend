from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.student_course_schema import StudentCreate, CourseCreate,StudentShape,CourseShape
from app.controllers import student_course_controller
import uuid

router = APIRouter(
    prefix="/studentCourse",
    tags=["StudentCourse"]
)

@router.get("/getAllCourses")
def getAllCourses(db:Session = Depends(get_db)):
    return student_course_controller.getAllCourses(db)

@router.get("/getAllStudents")
def getAllStudents(db:Session = Depends(get_db)):
    return student_course_controller.getAllStudents(db)

@router.post("/createStudent", response_model=StudentShape)
def createStudent(payload: StudentCreate,db:Session = Depends(get_db)):
    return student_course_controller.createStudent(db,payload)


@router.post("/createCouse", response_model=CourseShape)
def createCourse(payload: CourseCreate,db:Session = Depends(get_db)):
    return student_course_controller.createCourse(db,payload)


@router.post("/enrollCourse/{studentId}")
def enrollStudentToCourse(studentId:uuid.UUID,courseId: list[uuid.UUID],db:Session = Depends(get_db)):
    return student_course_controller.enrollStudentToCourse(db,studentId,courseId)

@router.get("/coursesEnrolled/{studentId}")
def courseEnrolled(studentId: uuid.UUID,db: Session = Depends(get_db)):
    return student_course_controller.courseEnrolled(db,studentId)

@router.get("/studentsErolled/{courseId}")
def studentEnrolled(courseId:uuid.UUID,db:Session = Depends(get_db)):
    return student_course_controller.studentEnrolled(db,courseId)