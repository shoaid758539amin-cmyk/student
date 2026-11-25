from fastapi import APIRouter, status
from service.student_service import StudentService
from utils.schema import StudentCreate, StudentUpdate

router = APIRouter(prefix="/students", tags=["Student"])


@router.get("/all", status_code=status.HTTP_200_OK)
def get_all_students():
    service = StudentService()
    return service.get_students()


@router.post("/add", status_code= status.HTTP_201_CREATED)
def add_student(student_payload: StudentCreate):
    service = StudentService()
    service.add_student(student_payload)

@router.delete("/delete/{student_roll}", status_code= status.HTTP_204_NO_CONTENT)
def delete_student(student_roll: int):
    service = StudentService()
    service.delete_student(student_roll)

@router.patch("/update/{student_roll}", status_code= status.HTTP_200_OK)
def update_student(student_roll: int, student_payload: StudentUpdate):
    service = StudentService()
    service.update_student(student_roll,student_payload)

