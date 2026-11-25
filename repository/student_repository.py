from sqlalchemy import delete
from sqlalchemy.orm import Session
from model.student import Students
from db import session_local

class StudentRepository:
    def __init__(self):
        self.connection = session_local()
    

    def get_all_student(self):
        return self.connection.query(Students).all()


    def create_student(self, student: Students):
        self.connection.add(student)
        self.connection.commit()

    def delete_student(self, student_roll: int):
        stmt = delete(Students).where(Students.roll == student_roll)
        self.connection.execute(stmt)
        self.connection.commit()

    def get_student_by_roll(self, roll: int):
        student = self.connection.query(Students).filter(Students.roll == roll).first()
        return student

    def update_student(self, model: Students):
        self.connection.merge(model)
        self.connection.commit()