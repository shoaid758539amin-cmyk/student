from sqlalchemy import delete

from db import session_local
from model.subjects import Subjects

class CourseRepository:
    def __init__(self):
        self.connection = session_local()

    def add_subject_score(self, subject: Subjects):
        self.connection.add(subject)
        self.connection.commit()

    def get_course_by_roll(self, roll : int):
        course_score = self.connection.query(Subjects).filter(Subjects.student_roll == roll).first()
        return course_score

    def delete_subject_score(self, student_roll: int):
        stmt = delete(Subjects).where(Subjects.student_roll == student_roll)
        self.connection.execute(stmt)
        self.connection.commit()


    def update_subject_score(self,  subject: Subjects):
        self.connection.merge(subject)
        self.connection.commit()
